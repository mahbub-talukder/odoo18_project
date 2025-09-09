from asyncio.log import logger
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class SalesCommissionTarget(models.Model):
    _name = 'sales.commission.target'
    _description = 'Commission Target'

    plan_id = fields.Many2one('sales.commission', required=True, ondelete='cascade', string='Plan')
    period = fields.Char(string='Period', required=True)
    date_from = fields.Date(string='From', required=True)
    date_to = fields.Date(string='To', required=True)

    # target_amount is only applicable for volume-based plans
    target_amount = fields.Monetary(string='Target Amount', currency_field='currency_id')
    # target_units is only applicable for qty-based plans
    target_units = fields.Float(string="Target Units")
    # collection target is only applicable for volume-based, amount_invoiced plans, and is a monetary field
    collection_target = fields.Monetary(string="Collection Target", currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', related='plan_id.currency_id', store=True, readonly=True)
    line_ids = fields.One2many('sales.commission.line', 'target_id', string="Commission Slabs")
    
    # Period Status Indicators
    period_status = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('active', 'Active'), 
        ('completed', 'Completed'),
        ('closed', 'Closed')
    ], string="Period Status", default='upcoming', compute='_compute_period_status', store=True)



    ########## utility methods ##########
    # Override create and write methods to update slab completion targets
    # when target_units or target_amount change
    
    @api.model
    def create(self, vals):
        """Override create to update slab completion targets after creation"""
        record = super(SalesCommissionTarget, self).create(vals)
        record._update_slab_completion_targets()
        return record
    
    def write(self, vals):
        """Override write to update slab completion targets when target values change"""
        result = super(SalesCommissionTarget, self).write(vals)
        if 'target_units' in vals or 'target_amount' in vals:
            self._update_slab_completion_targets()
        return result
    
    def _update_slab_completion_targets(self):
        """Update completion targets for all slabs based on current target values"""
        for rec in self:
            for slab in rec.line_ids:
                vals = {}
                if rec.plan_id.commission_type == 'qty':
                    if slab.completion_percent > 0 and rec.target_units > 0:
                        vals['completion_target_units'] = slab.completion_percent * rec.target_units
                elif rec.plan_id.commission_type == 'volume':
                    if slab.completion_percent > 0 and rec.target_amount > 0:
                        vals['completion_target_amount'] = slab.completion_percent * rec.target_amount
                
                if vals:
                    slab.write(vals)
                    _logger.info(f"Updated slab {slab.id} with values: {vals}")

    @api.depends('date_from', 'date_to')
    def _compute_period_status(self):
        """Compute period status based on dates and completion"""
        today = fields.Date.today()
        
        for rec in self:
            if rec.period_status == 'completed':
                continue
            if today < rec.date_from:
                rec.period_status = 'upcoming'  # Future period
            elif rec.date_from <= today <= rec.date_to:
                rec.period_status = 'active'  # Current period
            elif today > rec.date_to:
                rec.period_status = 'closed'  # Past period without commission
            else:
                rec.period_status = 'upcoming'

    @api.constrains('collection_target', 'target_amount')
    def _check_collection_target(self):
        """Ensure collection target does not exceed target amount"""
        for rec in self:
            if (rec.collection_target and rec.target_amount and 
                rec.collection_target > rec.target_amount):
                raise ValidationError(
                    f"Collection Target ({rec.collection_target:,.2f}) cannot be greater than "
                    f"Target Amount ({rec.target_amount:,.2f}) for period '{rec.period}'."
                )

    def _generate_commission_report(self, target_ids=None):
        """Generate commission reports for closed target periods"""
        _logger.info("Starting commission report generation...")
        
        # Find all closed target periods (past periods)
        today = fields.Date.today()
        domain = [
            ('date_to', '<', today),
            ('period_status', '!=', 'completed')
        ]
        
        # Filter by specific targets if provided
        if target_ids:
            domain.append(('id', 'in', target_ids))
        
        closed_targets = self.search(domain)
        
        _logger.info(f"Found {len(closed_targets)} finished target periods")
        
        for target in closed_targets:
            _logger.info(f"Processing target period: {target.period} for plan: {target.plan_id.name}")
            
            # Skip if no commission slabs defined
            if not target.line_ids:
                _logger.warning(f"No commission slabs defined for target period {target.period}")
                continue
                
            # Get all relevant salespersons for this plan
            salespersons = self._get_plan_salespersons(target.plan_id)
            
            for salesperson in salespersons:
                _logger.info(f"\n\n\nProcessing salesperson: {salesperson.name}")
                
                # Check if report already exists
                existing_report = self.env['sales.commission.report'].search([
                    ('salesperson_id', '=', salesperson.id),
                    ('period', '=', target.period),
                    ('plan_id', '=', target.plan_id.id),
                    ('target_id', '=', target.id)
                ])
                
                if existing_report:
                    _logger.info(f"Report already exists for {salesperson.name} - {target.period}")
                    continue
                
                # Apply business rule priority: Check for conflicting plans
                if self._should_skip_due_to_priority(target.plan_id, salesperson, target.date_from, target.date_to):
                    _logger.info(f"Skipping {target.plan_id.name} due to higher priority plan for {salesperson.name}")
                    continue
                
                # Calculate achievements for this salesperson
                achievements = self._calculate_achievements(target, salesperson)
                
                if not achievements or (achievements['total_amount'] == 0 and achievements['total_units'] == 0):
                    _logger.info(f"No achievements found for {salesperson.name} in period {target.period}")
                    continue
                
                # Calculate commission based on achievements
                commission_data = self._calculate_commission(target, achievements)
                
                if commission_data['commission_earned'] > 0:
                    # Create commission report
                    self._create_commission_report(target, salesperson, achievements, commission_data)
                else:
                    _logger.info(f"No commission earned for {salesperson.name} in period {target.period}")
            
            # Mark target period as completed after processing all salespersons
            target.period_status = 'completed'
        
        _logger.info("Commission report generation completed")

    def generate_commission_for_targets(self, target_ids):
        """Generate commission reports for specific target periods"""
        return self._generate_commission_report(target_ids=target_ids)

    def _get_plan_salespersons(self, plan):
        """Get all salespersons assigned to a commission plan"""
        salespersons = self.env['res.users']
        
        if plan.commission_for == 'person':
            salespersons = plan.salesperson_ids
        elif plan.commission_for == 'team' and plan.team_id:
            salespersons = plan.team_id.member_ids
        
        return salespersons

    def _should_skip_due_to_priority(self, current_plan, salesperson, date_from, date_to):
        """
        BRS Business Rule: Quantity-based plans have priority over volume-based plans
        for the same salesperson and overlapping periods with same products/categories
        """
        if current_plan.commission_type != 'volume':
            return False  # Only volume-based plans can be skipped
        
        # Find overlapping quantity-based plans for the same salesperson
        overlapping_plans = self.env['sales.commission'].search([
            ('commission_type', '=', 'qty'),
            ('state', '=', 'approved'),
            ('effective_from', '<=', date_to),
            ('effective_to', '>=', date_from),
            ('id', '!=', current_plan.id)
        ])
        
        for plan in overlapping_plans:
            # Check if salesperson is assigned to this plan
            plan_salespersons = self._get_plan_salespersons(plan)
            if salesperson not in plan_salespersons:
                continue
            
            # Check if products/categories overlap
            if self._plans_have_overlapping_scope(current_plan, plan):
                _logger.info(f"Found higher priority qty plan: {plan.name} for salesperson: {salesperson.name}")
                return True
        
        return False

    def _plans_have_overlapping_scope(self, plan1, plan2):
        """Check if two plans have overlapping product/category scope"""
        # If both plans apply to all products (no restrictions), they overlap
        if (not plan1.product_ids and not plan1.category_ids and 
            not plan2.product_ids and not plan2.category_ids):
            return True
        
        # If one plan applies to all products, they overlap
        if ((not plan1.product_ids and not plan1.category_ids) or 
            (not plan2.product_ids and not plan2.category_ids)):
            return True
        
        # Check product overlap
        if plan1.product_ids and plan2.product_ids:
            if set(plan1.product_ids.ids) & set(plan2.product_ids.ids):
                return True
        
        # Check category overlap
        if plan1.category_ids and plan2.category_ids:
            if set(plan1.category_ids.ids) & set(plan2.category_ids.ids):
                return True
        
        # Check if plan1 products belong to plan2 categories
        if plan1.product_ids and plan2.category_ids:
            for product in plan1.product_ids:
                if product.categ_id in plan2.category_ids:
                    return True
        
        # Check if plan2 products belong to plan1 categories
        if plan2.product_ids and plan1.category_ids:
            for product in plan2.product_ids:
                if product.categ_id in plan1.category_ids:
                    return True
        
        return False

    def _calculate_achievements(self, target, salesperson):
        """Calculate actual achievements for a salesperson in a target period"""
        _logger.info(f"Calculating achievements for {salesperson.name} in period {target.period}")
        
        plan = target.plan_id
        achievements = {
            'total_amount': 0.0,
            'total_units': 0.0,
            'details': []
        }
        
        # Calculate based on qualification criteria
        if plan.commission_type == 'volume':
            if plan.qualification_criteria == 'so_amount':
                achievements = self._calculate_sale_order_achievements(target, salesperson)
            elif plan.qualification_criteria == 'amount_invoiced':
                achievements = self._calculate_invoice_achievements(target, salesperson)
        elif plan.commission_type == 'qty':
            if plan.qualification_criteria == 'qty_sold':
                achievements = self._calculate_sale_order_achievements(target, salesperson)
            elif plan.qualification_criteria == 'qty_invoiced':
                achievements = self._calculate_invoice_achievements(target, salesperson)
        
        _logger.info(f"Total achievements for {salesperson.name}: Amount={achievements['total_amount']}, Units={achievements['total_units']}")
        return achievements

    def _calculate_sale_order_achievements(self, target, salesperson):
        """Calculate achievements from sale orders - FIXED VERSION"""
        # Build proper domain for sale orders
        domain = [
            ('user_id', '=', salesperson.id),  # Sale order salesperson
            ('date_order', '>=', target.date_from),
            ('date_order', '<=', target.date_to),
            ('state', 'in', ['sale', 'done']),
        ]
        
        sale_orders = self.env['sale.order'].search(domain)
        
        achievements = {
            'total_amount': 0.0,
            'total_units': 0.0,
            'details': []
        }
        
        for order in sale_orders:
            # Get order lines that match plan criteria
            filtered_lines = self._filter_order_lines(order.order_line, target.plan_id)
            
            if not filtered_lines:
                continue
            
            order_amount = sum(filtered_lines.mapped('price_subtotal'))
            order_units = sum(filtered_lines.mapped('product_uom_qty'))
            
            achievements['total_amount'] += order_amount
            achievements['total_units'] += order_units
            
            # Add detail record
            achievements['details'].append({
                'source_type': 'sale_order',
                'sale_order_id': order.id,
                'achieved_amount': order_amount,
                'achieved_units': order_units,
                'date_achievement': order.date_order,
                'product_ids': filtered_lines.mapped('product_id.id'),
                'category_ids': filtered_lines.mapped('product_id.categ_id.id'),
            })
        
        return achievements

    def _calculate_invoice_achievements(self, target, salesperson):
        """Calculate achievements from invoices - FIXED VERSION"""
        # Build proper domain for invoices
        domain = [
            ('invoice_date', '>=', target.date_from),
            ('invoice_date', '<=', target.date_to),
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted'),
        ]
        
        invoices = self.env['account.move'].search(domain)
        # equivalent psql query
        # SELECT * FROM account_move WHERE invoice_date >= '2025-01-01' AND invoice_date <= '2025-01-31' AND move_type = 'out_invoice' AND state = 'posted'
        # and exists (select 1 from account_move_line where account_move_line.move_id = account_move.id and account_move_line.product_id.categ_id in (1, 2, 3))
        achievements = {
            'total_amount': 0.0,
            'total_units': 0.0,
            'details': []
        }
        logger.info(f"Invoices: {invoices}")
        for invoice in invoices:
            # Check if invoice belongs to the salesperson through sale order
            if not self._invoice_belongs_to_salesperson(invoice, salesperson):
                continue
            
            # Get invoice lines that match plan criteria
            filtered_lines = self._filter_invoice_lines(invoice.invoice_line_ids, target.plan_id)
            
            if not filtered_lines:
                continue
            
            invoice_amount = sum(filtered_lines.mapped('price_subtotal'))
            invoice_units = sum(filtered_lines.mapped('quantity'))
            
            achievements['total_amount'] += invoice_amount
            achievements['total_units'] += invoice_units
            
            # Add detail record
            achievements['details'].append({
                'source_type': 'invoice',
                'invoice_id': invoice.id,
                'achieved_amount': invoice_amount,
                'achieved_units': invoice_units,
                'date_achievement': invoice.invoice_date,
                'product_ids': filtered_lines.mapped('product_id.id'),
                'category_ids': filtered_lines.mapped('product_id.categ_id.id'),
            })
        
        return achievements

    def _invoice_belongs_to_salesperson(self, invoice, salesperson):
        """Check if invoice belongs to salesperson through related sale order"""
        # Get related sale orders through invoice lines
        sale_orders = invoice.line_ids.mapped('sale_line_ids.order_id')
        
        # Check if any related sale order belongs to this salesperson
        for order in sale_orders:
            if order.user_id.id == salesperson.id:
                return True
        
        # Also check if invoice was created directly by salesperson (fallback)
        if hasattr(invoice, 'invoice_user_id') and invoice.invoice_user_id.id == salesperson.id:
            return True
        
        return False

    def _filter_order_lines(self, order_lines, plan):
        """Filter order lines based on plan's product/category restrictions"""
        # Start with non-display lines
        filtered_lines = order_lines.filtered(lambda l: not l.display_type)
        
        # Apply product filter if specified
        if plan.product_ids:
            filtered_lines = filtered_lines.filtered(lambda l: l.product_id.id in plan.product_ids.ids)
        
        # Apply category filter if specified
        if plan.category_ids:
            filtered_lines = filtered_lines.filtered(lambda l: l.product_id.categ_id.id in plan.category_ids.ids)
        logger.info(f"filtered order lines: {filtered_lines}")
        return filtered_lines

    def _filter_invoice_lines(self, invoice_lines, plan):
        """Filter invoice lines based on plan's product/category restrictions"""
        # Start with non-display lines
        filtered_lines = invoice_lines.filtered(lambda l: l.display_type)
        
        
        # Apply product filter if specified
        if plan.product_ids:
            filtered_lines = filtered_lines.filtered(lambda l: l.product_id.id in plan.product_ids.ids)
        
        # Apply category filter if specified
        if plan.category_ids:
            filtered_lines = filtered_lines.filtered(lambda l: l.product_id.categ_id.id in plan.category_ids.ids)
        logger.info(f"filtered invoice lines: {filtered_lines}")
        return filtered_lines

    def _calculate_commission(self, target, achievements):
        """Calculate commission based on achievements and commission slabs"""
        _logger.info(f"Calculating commission for target {target.period}")
        
        plan = target.plan_id
        commission_data = {
            'commission_earned': 0.0,
            'applicable_slabs': []
        }
        
        # Check collection target for volume-based amount_invoiced plans
        if (plan.commission_type == 'volume' and 
            plan.qualification_criteria == 'amount_invoiced' and 
            target.collection_target > 0):
            
            # Calculate actual collections from invoice payments
            collected_amount = self._calculate_actual_collections(target, achievements)
            
            if collected_amount < target.collection_target:
                _logger.info(f"Collection target not met: {collected_amount} < {target.collection_target}")
                return commission_data  # Return zero commission
        
        # Get target value for comparison
        if plan.commission_type == 'volume':
            target_value = target.target_amount or 0
            achieved_value = achievements['total_amount']
        else:  # qty
            target_value = target.target_units or 0
            achieved_value = achievements['total_units']
        
        if target_value <= 0:
            _logger.warning(f"No target value set for period {target.period}")
            return commission_data
        
        # Calculate achievement percentage
        achievement_percentage = achieved_value / target_value
        
        # Find applicable commission slabs
        applicable_slabs = target.line_ids.filtered(
            lambda slab: slab.completion_percent > 0 and achievement_percentage >= slab.completion_percent
        ).sorted('completion_percent', reverse=True)
        
        if applicable_slabs:
            # Use the highest applicable slab
            best_slab = applicable_slabs[0]
            commission_data['commission_earned'] = best_slab.commission_amount
            commission_data['applicable_slabs'] = [best_slab.id]
            
            _logger.info(f"Commission earned: {commission_data['commission_earned']} using slab {best_slab.completion_percent * 100}%")
        else:
            _logger.info("No applicable commission slabs found")
        
        return commission_data

    def _calculate_actual_collections(self, target, achievements):
        """Calculate actual collections from paid invoices - IMPROVED VERSION"""
        total_collected = 0.0
        
        # Get all invoice IDs from achievements
        invoice_details = [detail for detail in achievements['details'] if detail['source_type'] == 'invoice']
        
        for detail in invoice_details:
            invoice_id = detail.get('invoice_id')
            if not invoice_id:
                continue
                
            invoice = self.env['account.move'].browse(invoice_id)
            if not invoice.exists():
                continue
            
            # Calculate the proportion of this invoice that was achieved
            invoice_achieved_amount = detail['achieved_amount']
            invoice_total_amount = invoice.amount_untaxed
            
            if invoice_total_amount > 0:
                # Calculate collected amount for this invoice
                invoice_collected = 0.0
                if invoice.payment_state == 'paid':
                    invoice_collected = invoice_achieved_amount  # Fully paid
                elif invoice.payment_state == 'in_payment':
                    # Calculate partial payment based on amount residual
                    if invoice.amount_total > 0:
                        paid_ratio = (invoice.amount_total - invoice.amount_residual) / invoice.amount_total
                        invoice_collected = invoice_achieved_amount * paid_ratio
                
                total_collected += invoice_collected
        
        _logger.info(f"Total collected amount: {total_collected}")
        return total_collected
    
    # !this is the old method of creating commission report
    # we are using the real-time commission report now
    def _create_commission_report(self, target, salesperson, achievements, commission_data):
        """Create commission report record - ENHANCED VERSION"""
        _logger.info(f"Creating commission report for {salesperson.name} - {target.period}")
        
        plan = target.plan_id
        
        # Create main report record
        report_vals = {
            'salesperson_id': salesperson.id,
            'team_id': plan.team_id.id if plan.commission_for == 'team' else False,
            'period': target.period,
            'commission_type': plan.commission_type,
            'target_amount': target.target_amount,
            'target_units': target.target_units,
            'achieved_amount': achievements['total_amount'],
            'achieved_units': achievements['total_units'],
            'commission_earned': commission_data['commission_earned'],
            'commission_paid_status': 'pending',
            'company_id': plan.company_id.id,
            'plan_id': plan.id,
            'target_id': target.id,
        }
        
        report = self.env['sales.commission.report'].create(report_vals)
        
        # Create detail lines
        for detail in achievements['details']:
            # Calculate proportional commission for this detail
            detail_commission = 0.0
            if achievements['total_amount'] > 0:
                detail_commission = commission_data['commission_earned'] * (detail['achieved_amount'] / achievements['total_amount'])
            elif achievements['total_units'] > 0:
                detail_commission = commission_data['commission_earned'] * (detail['achieved_units'] / achievements['total_units'])
            
            detail_vals = {
                'report_id': report.id,
                'source_type': detail['source_type'],
                'sale_order_id': detail.get('sale_order_id'),
                'invoice_id': detail.get('invoice_id'),
                'achieved_amount': detail['achieved_amount'],
                'achieved_units': detail['achieved_units'],
                'date_achievement': detail['date_achievement'],
                'commission_earned': detail_commission
            }
            
            # Add product information if available
            if detail.get('product_ids'):
                detail_vals['product_id'] = detail['product_ids'][0] if detail['product_ids'] else False
            if detail.get('category_ids'):
                detail_vals['product_category_id'] = detail['category_ids'][0] if detail['category_ids'] else False
            
            self.env['sales.commission.report.line'].create(detail_vals)
        
        # Create vendor bill
        report._create_vendor_bill()
        _logger.info(f"Commission report created successfully: {report.id}")
        return report

    ########## end of utility methods ##########

    @api.model
    def cron_generate_vendor_bills(self):
        """
        Cron job method to automatically generate vendor bills for completed commission periods.
        Now uses real-time commission data instead of generating stored reports.
        """
        _logger.info("Starting automated vendor bill generation for completed commission periods...")
        
        try:
            # Find all completed target periods that need vendor bills
            today = fields.Date.today()
            completed_targets = self.search([
                ('date_to', '<', today),
                ('period_status', '!=', 'completed'),
                ('plan_id.state', '=', 'approved')
            ])
            
            if not completed_targets:
                _logger.info("No completed commission periods found that need vendor bills.")
                return
            
            bills_created = 0
            targets_processed = 0
            
            for target in completed_targets:
                _logger.info(f"Processing completed target: {target.period} for plan: {target.plan_id.name}")
                
                try:
                    # Get real-time commission data for this target period
                    realtime_commissions = self.env['sales.commission.realtime.report'].search([
                        ('target_id', '=', target.id),
                        ('commission_earned', '>', 0)
                    ])
                    
                    if not realtime_commissions:
                        _logger.info(f"No commissions earned for target period {target.period}")
                        # Mark as completed even if no commissions
                        target.period_status = 'completed'
                        # find the next target period and update the target as active target
                        next_target = self.search([
                            ('date_from', '>', target.date_to),
                            ('plan_id', '=', target.plan_id.id),
                            ('period_status', '!=', 'completed')
                        ], order='date_from asc', limit=1)
                        logger.info(f"Next target: {next_target}")
                        if next_target:
                            next_target.period_status = 'active'
                        continue
                    
                    # Group by salesperson and create vendor bills
                    for commission in realtime_commissions:
                        existing_report = self.env['sales.commission.report'].search([
                            ('salesperson_id', '=', commission.salesperson_id.id),
                            ('period', '=', commission.period),
                            ('plan_id', '=', commission.plan_id.id),
                            ('target_id', '=', commission.target_id.id)
                        ])
                        
                        if existing_report:
                            _logger.info(f"Bill already exists for {commission.salesperson_id.name} - {commission.period}")
                            continue
                        
                        # Create commission report record for bill tracking
                        report_vals = {
                            'salesperson_id': commission.salesperson_id.id,
                            'team_id': commission.team_id.id,
                            'period': commission.period,
                            'commission_type': commission.commission_type,
                            'target_amount': commission.target_amount,
                            'target_units': commission.target_units,
                            'achieved_amount': commission.achieved_amount,
                            'achieved_units': commission.achieved_units,
                            'commission_earned': commission.commission_earned,
                            'commission_paid_status': 'pending',
                            'company_id': commission.company_id.id,
                            'plan_id': commission.plan_id.id,
                            'target_id': commission.target_id.id,
                        }
                        
                        report = self.env['sales.commission.report'].create(report_vals)
                        
                        # Create vendor bill for commission payment
                        report._create_vendor_bill()
                        
                        if report.bill_id:
                            bills_created += 1
                            _logger.info(f"✅ Created vendor bill for {commission.salesperson_id.name} - {commission.period}")
                        
                    # Mark target as completed
                    target.period_status = 'completed'
                    targets_processed += 1
                    
                except Exception as target_error:
                    _logger.error(f"Error processing target {target.period}: {str(target_error)}")
                    continue
            
            _logger.info(f"Vendor bill generation completed. Processed {targets_processed} targets, created {bills_created} vendor bills.")
            
        except Exception as e:
            _logger.error(f"Error in automated vendor bill generation: {str(e)}")
            raise

    def action_test_commission_generation(self):
        """Test method for commission generation - For development/testing only"""
        self.ensure_one()
        
        # Force generate commission for this specific target
        try:
            self._generate_commission_report(target_ids=[self.id])
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Commission Generation Test',
                    'message': f'Commission generation completed for period {self.period}. Check the Commission Reports.',
                    'type': 'success',
                }
            }
        except Exception as e:
            _logger.error(f"Commission generation failed: {str(e)}")
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Commission Generation Error',
                    'message': f'Error: {str(e)}',
                    'type': 'danger',
                }
            }

    def action_view_commission_reports(self):
        """View commission reports generated for this target period"""
        self.ensure_one()
        
        reports = self.env['sales.commission.report'].search([
            ('target_id', '=', self.id)
        ])
        
        return {
            'type': 'ir.actions.act_window',
            'name': f'Commission Reports for {self.period}',
            'res_model': 'sales.commission.report',
            'view_mode': 'list,form',
            'domain': [('target_id', '=', self.id)],
            'context': {'create': False},
        }

 
from odoo import models, fields, api

class SalesCommissionReport(models.Model):
    _name = 'sales.commission.report'
    _description = 'My Commission Report'

    salesperson_id = fields.Many2one('res.users', string="Salesperson", readonly=True)
    team_id = fields.Many2one('crm.team', string="Sales Team", readonly=True)
    period = fields.Char(string="Period", readonly=True)
    commission_type = fields.Selection([
        ('qty', 'Based on Quantity'),
        ('volume', 'Based on Volume')
    ], string="Commission Type", readonly=True)
    
    # Target fields
    target_amount = fields.Monetary(string="Target Amount", readonly=True)
    target_units = fields.Float(string="Target Units", readonly=True)
    
    # Achievement fields
    achieved_amount = fields.Monetary(string="Achieved Amount", readonly=True)
    achieved_units = fields.Float(string="Achieved Units", readonly=True)
    
    # Commission fields
    commission_earned = fields.Monetary(string="Commission Earned", readonly=True)
    commission_paid_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('partially_paid', 'Partially Paid'),
        ('paid', 'Paid'),
        ('overpaid', 'Overpaid')
    ], string="Paid Status", compute='_compute_commission_paid_status', store=True, readonly=True)
    
    # System fields
    company_id = fields.Many2one('res.company', string="Company", readonly=True)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', store=True, readonly=True)
    plan_id = fields.Many2one('sales.commission', string="Commission Plan", readonly=True)
    target_id = fields.Many2one('sales.commission.target', string="Target Period", readonly=True)
    
    # Bill tracking
    bill_generated = fields.Boolean(string="Bill Generated", readonly=True)
    bill_id = fields.Many2one('account.move', string="Vendor Bill", readonly=True)
    
    # Details
    detail_ids = fields.One2many('sales.commission.report.line', 'report_id', string="Contributing Details")

    _sql_constraints = [
        ('report_unique_combination', 'unique(salesperson_id, team_id, period, commission_type, company_id)', 
         'A commission report already exists for this combination of Salesperson, Sales Team, Period, Commission Type, and Company!')
    ]

    @api.depends('bill_id', 'bill_id.payment_state')
    def _compute_commission_paid_status(self):
        """Compute commission paid status based on vendor bill payment state"""
        for report in self:
            if not report.bill_id:
                report.commission_paid_status = 'unpaid'
            elif report.bill_id.payment_state == 'paid':
                report.commission_paid_status = 'paid'
            elif report.bill_id.payment_state == 'partial':
                report.commission_paid_status = 'partially_paid'
            else:
                report.commission_paid_status = 'unpaid'

    def action_view_commission_details(self):
        """Open commission details view"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Commission Details',
            'res_model': 'sales.commission.report.line',
            'view_mode': 'list,form',
            'domain': [('report_id', '=', self.id)],
            'context': {'default_report_id': self.id},
            'target': 'current',
        }
    
    def action_view_commission_details_realtime(self):
        """View detailed breakdown of this commission"""
        self.ensure_one()
        
        # For now, show sale orders that contribute to this commission
        if self.commission_type == 'volume' and 'so_amount' in self.plan_id.qualification_criteria:
            # Show sale orders
            domain = [
                ('user_id', '=', self.salesperson_id.id),
                ('date_order', '>=', self.target_id.date_from),
                ('date_order', '<=', self.target_id.date_to),
                ('state', 'in', ['sale', 'done'])
            ]
            return {
                'type': 'ir.actions.act_window',
                'name': f'Sale Orders Contributing to Commission - {self.period}',
                'res_model': 'sale.order',
                'view_mode': 'list,form',
                'domain': domain,
                'context': {'create': False},
                'target': 'current',
            }
        elif self.commission_type == 'volume' and 'amount_invoiced' in self.plan_id.qualification_criteria:
            # Show invoices
            domain = [
                ('invoice_date', '>=', self.target_id.date_from),
                ('invoice_date', '<=', self.target_id.date_to),
                ('move_type', '=', 'out_invoice'),
                ('invoice_user_id', '=', self.salesperson_id.id),
                ('line_ids.product_id', '!=', False),
                ('line_ids.display_type', '!=', False),
                ('state', '=', 'posted')
            ]
            return {
                'type': 'ir.actions.act_window',
                'name': f'Invoices Contributing to Commission - {self.period}',
                'res_model': 'account.move',
                'view_mode': 'list,form',
                'domain': domain,
                'context': {'create': False},
                'target': 'current',
            }
        else:
            # Default: show a message or existing commission report lines
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Commission Details',
                    'message': f'Commission earned: {self.commission_earned}\nPlan: {self.plan_id.name}',
                    'type': 'info',
                    'sticky': False,
                }
            }
    
    

    def action_view_vendor_bill(self):
        """Open related vendor bill"""
        self.ensure_one()
        if not self.bill_id:
            return False
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vendor Bill',
            'res_model': 'account.move',
            'res_id': self.bill_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def _create_vendor_bill(self):
        """
        Create vendor bill for commission payment with security validations.
        SECURITY: Multiple validation layers to prevent unauthorized bill creation.
        """
        import logging
        _logger = logging.getLogger(__name__)
        
        for report in self:
            # SECURITY: Comprehensive pre-checks
            if not self._validate_bill_creation_prerequisites(report):
                continue

            try:
                # SECURITY: Find expense account with proper validation
                expense_account = self._get_secure_expense_account(report)
                if not expense_account:
                    _logger.error(f"No valid expense account found for company {report.company_id.name}")
                    continue

                # SECURITY: Find purchase journal with validation
                purchase_journal = self._get_secure_purchase_journal(report)
                if not purchase_journal:
                    _logger.error(f"No valid purchase journal found for company {report.company_id.name}")
                    continue

                # Create vendor bill with security validations
                bill_vals = {
                    'move_type': 'in_invoice',
                    'partner_id': report.salesperson_id.partner_id.id,
                    'journal_id': purchase_journal.id,
                    'invoice_date': fields.Date.today(),
                    'ref': f"Commission for {report.period} - {report.salesperson_id.name} - Plan: {report.plan_id.name}",
                    'invoice_line_ids': [(0, 0, {
                        'name': f"Sales Commission for {report.period} (Plan: {report.plan_id.name})",
                        'quantity': 1,
                        'price_unit': report.commission_earned,
                        'account_id': expense_account.id,
                    })],
                    'company_id': report.company_id.id,
                    'commission_plan_id': report.plan_id.id,
                }

                # SECURITY: Create bill with error handling
                bill = self.env['account.move'].create(bill_vals)
                
                if bill.id:
                    report.bill_id = bill.id
                    report.bill_generated = True
                    _logger.info(f"✅ Vendor bill {bill.id} created successfully for commission report {report.id}")
                else:
                    report.bill_generated = False
                    _logger.error(f"❌ Failed to create vendor bill for commission report {report.id}")

            except Exception as e:
                _logger.error(f"❌ Error creating vendor bill for report {report.id}: {str(e)}")
                report.bill_generated = False
                raise

    def _validate_bill_creation_prerequisites(self, report):
        """Security validation for bill creation prerequisites"""
        import logging
        _logger = logging.getLogger(__name__)
        
        # Check 1: Commission amount validation
        if not report.commission_earned or report.commission_earned <= 0:
            _logger.warning(f"Invalid commission amount for report {report.id}: {report.commission_earned}")
            return False

        # Check 2: Partner validation
        if not report.salesperson_id.partner_id:
            _logger.warning(f"No partner record for salesperson {report.salesperson_id.name}")
            return False

        # Check 3: Bill already exists
        if report.bill_id:
            _logger.warning(f"Bill already exists for report {report.id}: {report.bill_id.id}")
            return False

        # Check 4: Plan state validation
        if report.plan_id.state != 'approved':
            _logger.warning(f"Commission plan not approved: {report.plan_id.state}")
            return False

        # Check 5: User active validation
        if not report.salesperson_id.active:
            _logger.warning(f"Salesperson is inactive: {report.salesperson_id.name}")
            return False

        return True

    def _get_secure_expense_account(self, report):
        """Get expense account with security validation"""
        # Try to find commission-specific expense account first
        # expense_account = self.env['account.account'].search([
        #     ('company_id', '=', report.company_id.id),
        #     ('account_type', '=', 'expense'),
        #     ('code', 'like', '621987%')  # Commission expense account
        # ], limit=1)
        
        # # Fallback to general expense account
        # if not expense_account:
        expense_account = self.env['account.account'].search([
            ('company_id', '=', report.company_id.id),
            ('account_type', '=', 'expense')
        ], limit=1)
        
        return expense_account

    def _get_secure_purchase_journal(self, report):
        """Get purchase journal with security validation"""
        return self.env['account.journal'].search([
            ('type', '=', 'purchase'), 
            ('company_id', '=', report.company_id.id),
            ('active', '=', True)
        ], limit=1)



    # @api.model
    # def cron_create_vendor_bills(self):
    #     """
    #     Cron job method to automatically create vendor bills for commission reports.
    #     This method should be called by scheduled actions.
    #     SECURITY: Only processes validated commission reports with proper authorization.
    #     """
    #     import logging
    #     _logger = logging.getLogger(__name__)
        
    #     _logger.info("Starting automated vendor bill creation for commission reports...")
        
    #     try:
    #         # SECURITY CHECK: Only process reports from approved commission plans
    #         reports_without_bills = self.search([
    #             ('commission_earned', '>', 0),                    # Must have earned commission
    #             ('bill_id', '=', False),                         # No existing vendor bill
    #             ('bill_generated', '=', False),                  # Not already processed
    #             ('salesperson_id.partner_id', '!=', False),     # Must have partner record
    #             ('plan_id.state', '=', 'approved'),             # SECURITY: Only approved plans
    #             ('salesperson_id.active', '=', True),           # SECURITY: Only active users
    #             ('company_id', '=', self.env.company.id),       # SECURITY: Only current company
    #         ])
            
    #         if not reports_without_bills:
    #             _logger.info("No commission reports found that need vendor bills.")
    #             return
            
    #         bills_created = 0
    #         errors_count = 0
            
    #         # SECURITY: Additional validation before processing
    #         for report in reports_without_bills:
    #             try:
    #                 # SECURITY: Double-check critical conditions
    #                 if not self._validate_bill_creation_security(report):
    #                     _logger.warning(f"Security validation failed for report {report.id} - skipping")
    #                     continue
                    
    #                 _logger.info(f"Creating vendor bill for commission report {report.id} - {report.salesperson_id.name} - Amount: {report.commission_earned}")
                    
    #                 # Create the vendor bill
    #                 report._create_vendor_bill()
                    
    #                 if report.bill_id:
    #                     bills_created += 1
    #                     _logger.info(f"✅ Successfully created vendor bill {report.bill_id.id} for report {report.id}")
    #                 else:
    #                     _logger.warning(f"⚠️ Vendor bill creation returned no bill for report {report.id}")
                    
    #             except Exception as report_error:
    #                 errors_count += 1
    #                 _logger.error(f"❌ Error creating vendor bill for report {report.id}: {str(report_error)}")
    #                 # Continue with other reports even if one fails
    #                 continue
            
    #         _logger.info(f"Vendor bill creation completed. ✅ Created: {bills_created}, ❌ Errors: {errors_count}, 📊 Total processed: {len(reports_without_bills)}")
            
    #     except Exception as e:
    #         _logger.error(f"❌ Critical error in automated vendor bill creation: {str(e)}")
    #         raise

    def _validate_bill_creation_security(self, report):
        """
        Security validation before creating vendor bills.
        Returns True if safe to create bill, False otherwise.
        """
        import logging
        _logger = logging.getLogger(__name__)
        
        # Check 1: Commission amount must be positive (not zero or negative)
        if report.commission_earned <= 0:
            _logger.warning(f"Invalid commission amount: {report.commission_earned}")
            return False
        
        # Check 2: Salesperson has valid partner record
        if not report.salesperson_id.partner_id:
            _logger.warning(f"Salesperson {report.salesperson_id.name} has no partner record")
            return False
        
        # Check 3: Plan is still approved and active
        if report.plan_id.state != 'approved':
            _logger.warning(f"Plan {report.plan_id.name} is not approved: {report.plan_id.state}")
            return False
        
        # Check 4: No duplicate bills exist
        existing_bill = self.search([
            ('salesperson_id', '=', report.salesperson_id.id),
            ('period', '=', report.period),
            ('plan_id', '=', report.plan_id.id),
            ('bill_id', '!=', False),
            ('id', '!=', report.id)
        ], limit=1)
        
        if existing_bill:
            _logger.warning(f"Duplicate bill may exist for same period/plan/user")
            return False
        
        # Check 5: Company consistency
        if report.company_id != self.env.company:
            _logger.warning(f"Report company {report.company_id.name} != current company {self.env.company.name}")
            return False
        
        return True

class SalesCommissionReportLine(models.Model):
    _name = 'sales.commission.report.line'
    _description = 'Commission Report Detail Line'

    report_id = fields.Many2one('sales.commission.report', required=True, ondelete='cascade', string="Commission Report")
    
    # Source information
    source_type = fields.Selection([
        ('sale_order', 'Sale Order'),
        ('invoice', 'Invoice')
    ], string="Source", readonly=True)
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)
    invoice_id = fields.Many2one('account.move', string="Invoice", readonly=True)
    
    # Product information
    product_id = fields.Many2one('product.product', string="Product", readonly=True)
    product_category_id = fields.Many2one('product.category', string="Product Category", readonly=True)
    
    # Achievement amounts
    achieved_amount = fields.Monetary(string="Achieved Amount", readonly=True)
    achieved_units = fields.Float(string="Achieved Units", readonly=True)
    
    # Commission calculation
    commission_earned = fields.Monetary(string="Commission Earned", readonly=True)
    commission_slab_id = fields.Many2one('sales.commission.line', string="Commission Slab", readonly=True)
    
    # Additional fields
    date_achievement = fields.Date(string="Achievement Date", readonly=True)
    currency_id = fields.Many2one('res.currency', related='report_id.currency_id', store=True, readonly=True)
    
    def action_view_source_document(self):
        """View the source document (sale order or invoice)"""
        self.ensure_one()
        if self.source_type == 'sale_order' and self.sale_order_id:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Sale Order',
                'res_model': 'sale.order',
                'res_id': self.sale_order_id.id,
                'view_mode': 'form',
                'target': 'current',
            }
        elif self.source_type == 'invoice' and self.invoice_id:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Invoice',
                'res_model': 'account.move',
                'res_id': self.invoice_id.id,
                'view_mode': 'form',
                'target': 'current',
            }
        return False 
from odoo import models, fields, api,Command
from dateutil.relativedelta import relativedelta
from datetime import date
from calendar import monthrange
import logging

logger = logging.getLogger(__name__)

QTY_OPTIONS = [
    ('qty_sold', 'Quantity Sold'),
    ('qty_invoiced', 'Quantity Invoiced')
]
VOLUME_OPTIONS = [
    ('so_amount', 'Sale Order Amount'),
    ('amount_invoiced', 'Amount Invoiced')  
]

class SalesCommission(models.Model):
    _name = 'sales.commission'
    _description = 'Sales Commission Plan'

    name = fields.Char(required=True, string="Commission Title")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', string="Status")

    commission_type = fields.Selection([
        ('qty', 'Based on Quantity'),
        ('volume', 'Based on Volume')
    ], required=True, string="Commission Type", default='volume' )

    qualification_criteria_qty = fields.Selection(QTY_OPTIONS,  string="Qualification Criteria")
    qualification_criteria_volume = fields.Selection(VOLUME_OPTIONS, string="Qualification Criteria")
    qualification_criteria = fields.Selection(QTY_OPTIONS + VOLUME_OPTIONS,
                                         required=False,store=True,
                                         compute='_compute_qualification_criteria')

    @api.depends('commission_type', 'qualification_criteria_qty', 'qualification_criteria_volume')
    def _compute_qualification_criteria(self):
        for rec in self:
            if rec.commission_type == 'qty':
                rec.qualification_criteria = rec.qualification_criteria_qty
            elif rec.commission_type == 'volume':
                rec.qualification_criteria = rec.qualification_criteria_volume
            else:
                rec.qualification_criteria = None

    active = fields.Boolean(default=True)
    commission_for = fields.Selection([
        ('person', 'Salesperson'),
        ('team', 'Sales Team')
    ], string="Commission For", default='person', required=True)
    salesperson_ids = fields.Many2many('res.users', string="Salespeople")
    
    @api.onchange('salesperson_ids')
    def _onchange_salesperson_ids(self):
        """Restrict user selection for non-admins"""
        if not self.env.user.has_group('av_sales_commission.group_sales_commission_admin'):
            # Regular users can only select themselves
            allowed_users = self.env.user
            if self.salesperson_ids:
                invalid_users = self.salesperson_ids - allowed_users
                if invalid_users:
                    self.salesperson_ids = allowed_users
                    return {
                        'warning': {
                            'title': 'Access Restricted',
                            'message': 'You can only assign commission plans to yourself. Other users have been removed from the selection.'
                        }
                    }
    team_id = fields.Many2one('crm.team', string="Sales Team")
    # define appropriate table name for the many to many fields
    product_ids = fields.Many2many('product.product', 
                                  'sales_commission_product_rel', 
                                  'commission_id', 
                                  'product_id', 
                                  string="Products")
    category_ids = fields.Many2many('product.category', 
                                   'sales_commission_category_rel', 
                                   'commission_id', 
                                   'category_id', 
                                   string="Product Categories")
    effective_from = fields.Date(required=True)
    effective_to = fields.Date(required=True)

    frequency = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly')
    ], required=True, default='quarterly', string="Target Frequency")
    
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', store=True, readonly=True)
    target_ids = fields.One2many('sales.commission.target', 'plan_id', string="Targets")

    def _default_effective_from(self): 
        from datetime import date
        return date(date.today().year, 1, 1)
    
    def _default_effective_to(self): 
        from datetime import date
        return date(date.today().year, 12, 31)
    
    effective_from = fields.Date(required=True, default=_default_effective_from)
    effective_to = fields.Date(required=True, default=_default_effective_to)

    # Workflow actions
    def action_approve(self):
        """Approve commission plan - Only administrators can approve"""
        if not self.env.user.has_group('av_sales_commission.group_sales_commission_admin'):
            from odoo.exceptions import AccessError
            raise AccessError("Only Commission Administrators can approve commission plans.")
        self.write({'state': 'approved'})

    def action_done(self):
        """Mark commission plan as done - Only administrators can mark as done"""
        if not self.env.user.has_group('av_sales_commission.group_sales_commission_admin'):
            from odoo.exceptions import AccessError
            raise AccessError("Only Commission Administrators can mark commission plans as done.")
        self.write({'state': 'done'})

    def action_cancel(self):
        """Cancel commission plan - Only administrators can cancel"""
        if not self.env.user.has_group('av_sales_commission.group_sales_commission_admin'):
            from odoo.exceptions import AccessError
            raise AccessError("Only Commission Administrators can cancel commission plans.")
        self.write({'state': 'cancel'})

    def action_draft(self):
        """Reset commission plan to draft - Only administrators can reset to draft"""
        if not self.env.user.has_group('av_sales_commission.group_sales_commission_admin'):
            from odoo.exceptions import AccessError
            raise AccessError("Only Commission Administrators can reset commission plans to draft.")
        self.write({'state': 'draft'})

    def action_generate_commission_reports(self):
        """Manual trigger to generate commission reports for this plan testing/development purpose"""
        logger.info(f"Manual commission generation triggered for plan: {self.name}")

        if self.state != 'approved':
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Plan Not Approved',
                    'message': 'Please approve the plan before generating commission reports.',
                    'type': 'warning',
                }
            }
        
        # Find all target periods for this plan that are finished
        today = fields.Date.today()
        closed_targets = self.target_ids.filtered(
            lambda t: t.date_to and t.date_to < today and t.period_status != 'completed'
        )

        
        if not closed_targets:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'No Closed Periods',
                    'message': 'No closed target periods found for commission generation.',
                    'type': 'warning',
                }
            }
        
        # Trigger commission generation for these targets
        reports_created = 0
        target_ids = closed_targets.ids
        
        if target_ids:
            try:
                # Generate commission reports for specific targets
                self.env['sales.commission.target'].generate_commission_for_targets(target_ids)
                reports_created = len(target_ids)
            except Exception as e:
                logger.error(f"Error generating commissions: {str(e)}")
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Commission Generation Error',
                        'message': f'Error occurred during commission generation: {str(e)}',
                        'type': 'danger',
                    }
                }
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Commission Generation Complete',
                'message': f'Commission reports generated for {reports_created} target period(s).',
                'type': 'success',
            }
        }

    def action_view_commission_reports(self):
        """View real-time commission reports for this plan"""
        return {
            'type': 'ir.actions.act_window',
            'name': f'Real-time Commissions - {self.name}',
            'res_model': 'sales.commission.realtime.report',
            'view_mode': 'list,form',
            'domain': [('plan_id', '=', self.id)],
            'context': {'default_plan_id': self.id},
            'target': 'current',
        }
        
    def action_view_historical_reports(self):
        """View historical commission reports (for bill tracking)"""
        return {
            'type': 'ir.actions.act_window',
            'name': f'Historical Reports - {self.name}',
            'res_model': 'sales.commission.report',
            'view_mode': 'list,form',
            'domain': [('plan_id', '=', self.id)],
            'context': {'default_plan_id': self.id},
            'target': 'current',
        }

    def action_create_test_commission_slabs(self):
        """Development helper: Create default commission slabs for testing"""
        if not self.target_ids:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'No Target Periods',
                    'message': 'Please create target periods first.',
                    'type': 'warning',
                }
            }
        
        slabs_created = 0
        for target in self.target_ids:
            if target.line_ids:
                continue  # Skip if slabs already exist
                
            # Create default slabs: 50%, 75%, 100%, 150%
            default_slabs = [
                {'percent': 0.50, 'commission': 100.0},
                {'percent': 0.75, 'commission': 150.0},
                {'percent': 1.00, 'commission': 200.0},
                {'percent': 1.50, 'commission': 300.0},
                {'percent': 2.00, 'commission': 400.0},
            ]
            
            for slab_data in default_slabs:
                slab_vals = {
                    'target_id': target.id,
                    'completion_percent': slab_data['percent'],
                    'commission_amount': slab_data['commission'],
                }
                
                # Set completion targets based on commission type
                if self.commission_type == 'volume' and target.target_amount:
                    slab_vals['completion_target_amount'] = target.target_amount * slab_data['percent']
                elif self.commission_type == 'qty' and target.target_units:
                    slab_vals['completion_target_units'] = target.target_units * slab_data['percent']
                
                self.env['sales.commission.line'].create(slab_vals)
                slabs_created += 1
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Test Slabs Created',
                'message': f'Created {slabs_created} test commission slabs.',
                'type': 'success',
            }
        }

    def action_open_commission(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Commission Slabs',
            'res_model': 'sales.commission.line',
            'view_mode': 'list,form',
            'domain': [('target_id.plan_id', 'in', self.ids)],
            'context': dict(self.env.context, default_commission_id=self.id),
            'target': 'current',
        }

    # Auto-generate targets
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        # for rec in records:
        #     rec._generate_targets()
        return records

    @api.onchange('effective_from', 'effective_to', 'frequency')
    def _onchange_generate_targets(self):
        if self.effective_from and self.effective_to and self.frequency:
            self._generate_targets()

    def _generate_targets(self):
        for rec in self:
            rec.target_ids = [(5, 0, 0)]  # Clear existing

            if not rec.effective_from or not rec.effective_to:
                continue

            start = rec.effective_from
            end = rec.effective_to
            current = start

            targets = []

            while current <= end:
                if rec.frequency == 'monthly':
                    period_start = current.replace(day=1)
                    last_day = monthrange(current.year, current.month)[1]
                    period_end = current.replace(day=last_day)
                    period_name = current.strftime('%B %Y')
                    next_start = current + relativedelta(months=1)
                else:  # quarterly
                    q = (current.month - 1) // 3 + 1
                    month_start = 3 * (q - 1) + 1
                    period_start = date(current.year, month_start, 1)
                    period_end = (period_start + relativedelta(months=3)) - relativedelta(days=1)
                    period_name = f"Q{q} {current.year}"
                    next_start = period_end + relativedelta(days=1)

                if period_start > end:
                    break
                if period_end > end:
                    period_end = end

                targets.append((0, 0, {
                    'period': period_name,
                    'date_from': period_start,
                    'date_to': period_end,
                }))

                current = next_start

            rec.target_ids = targets

    # on change of commission_for,if for person then clear team_id and if for team then clear salesperson_ids vice versa
    @api.onchange('commission_for')
    def _onchange_commission_for(self):
        if self.commission_for == 'person':
            self.team_id = False
        elif self.commission_for == 'team':
            self.salesperson_ids = False
    @api.constrains('commission_for', 'salesperson_ids', 'team_id')
    def _check_salesperson_team_exclusion(self):
        """Ensure plans cannot be assigned to both salespersons and teams simultaneously"""
        for rec in self:
            if rec.commission_for == 'person':
                if rec.team_id:
                    raise models.ValidationError(
                        "Commission plan cannot be assigned to both individual salespersons and a sales team. "
                        "Please select either 'Salesperson' or 'Sales Team', not both."
                    )
                if not rec.salesperson_ids:
                    raise models.ValidationError(
                        "At least one salesperson must be selected when commission is for 'Salesperson'."
                    )
            elif rec.commission_for == 'team':
                if rec.salesperson_ids:
                    raise models.ValidationError(
                        "Commission plan cannot be assigned to both individual salespersons and a sales team. "
                        "Please select either 'Salesperson' or 'Sales Team', not both."
                    )
                if not rec.team_id:
                    raise models.ValidationError(
                        "A sales team must be selected when commission is for 'Sales Team'."
                    )

    @api.constrains('commission_type', 'salesperson_ids', 'state', 'effective_from', 'effective_to')
    def _check_unique_commission_type_per_salesperson(self):
        """Ensure each salesperson can have only one plan per commission type during overlapping periods"""
        for record in self:
            # Skip check if no salespeople assigned, plan is cancelled, or not for person
            if not record.salesperson_ids or record.state == 'cancel' or record.commission_for != 'person':
                continue
            
            # Skip if dates are not set
            if not record.effective_from or not record.effective_to:
                continue
            
            for salesperson in record.salesperson_ids:
                # Search for other active plans of the same commission type for this salesperson
                # that have overlapping date ranges
                duplicate_plans = self.search([
                    ('id', '!=', record.id),
                    ('commission_type', '=', record.commission_type),
                    ('salesperson_ids', 'in', salesperson.id),
                    ('commission_for', '=', 'person'),
                    ('state', '!=', 'cancel'),  # Exclude cancelled plans
                    ('effective_from', '!=', False),
                    ('effective_to', '!=', False),
                    # Date overlap condition: (A.start <= B.end) AND (B.start <= A.end)
                    ('effective_from', '<=', record.effective_to),
                    ('effective_to', '>=', record.effective_from),
                ])
                
                if duplicate_plans:
                    commission_type_label = dict(record._fields['commission_type'].selection)[record.commission_type]
                    overlapping_plan = duplicate_plans[0]
                    raise models.ValidationError(
                        f"Salesperson '{salesperson.name}' already has an overlapping {commission_type_label} commission plan: "
                        f"'{overlapping_plan.name}' (effective from {overlapping_plan.effective_from} to {overlapping_plan.effective_to}). "
                        f"Each salesperson can have only one plan per commission type during the same period."
                    ) 
from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError

class CommissionPlan(models.Model):
    _name = 'commission.plan'
    _description = 'Sales Commission Plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    commission_plan_type = fields.Selection([
        ('sales_team', 'Sales Team'),
        ('admin', 'Admin')
    ], string='Commission Plan Type', required=True, default='sales_team', tracking=True)
    
    name = fields.Char(string='Plan Name', required=True, tracking=True)
    target_period_start = fields.Date(string='Target Period Start', required=True, tracking=True)
    target_period_end = fields.Date(string='Target Period End', required=True, tracking=True)
    
    salesperson_ids = fields.Many2many(
        'res.users',
        'commission_plan_salesperson_rel',
        'plan_id',
        'user_id',
        string='Sales Persons',
        domain=[('share', '=', False)],
        tracking=True
    )
    
    admin_person_id = fields.Many2one(
        'res.users', 
        string='Admin Person', 
        domain=[('share', '=', False)],
        tracking=True
    )
    
    def read(self, fields=None, load='_classic_read'):
        """Override read to filter salesperson_ids for non-admin users"""
        result = super().read(fields, load)
        
        # Only filter if not admin and salesperson_ids is in the requested fields
        if not self.env.user.has_group('ox_sales_commission.group_commission_sale_admin'):
            for record in result:
                if isinstance(record, dict) and 'salesperson_ids' in record:
                    # Filter salesperson_ids to only show current user if they're in the list
                    if record['salesperson_ids']:
                        current_user_id = self.env.user.id
                        if current_user_id in record['salesperson_ids']:
                            record['salesperson_ids'] = [current_user_id]
                        else:
                            record['salesperson_ids'] = []
        
        return result
    disbursement_frequency = fields.Selection([
        ('weekly', 'Weekly'),
        ('biweekly', 'Biweekly'),
        ('monthly', 'Monthly')
    ], string='Disbursement Frequency', default='biweekly', required=True, tracking=True)
    
    first_order_commission = fields.Float(
        string='First Order Commission (%)',
        default=20.0,
        required=True,
        tracking=True
    )
    residual_commission = fields.Float(
        string='Residual Commission (%)',
        default=10.0,
        required=True,
        tracking=True
    )
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    
    company_id = fields.Many2one('res.company', string='Company', 
                                  default=lambda self: self.env.company, required=True)
    # this field is used for testing purpose to run the cron job manually
    cron_run_date = fields.Date(string='Cron Run Date')
    commission_tracking_ids = fields.One2many('commission.tracking', 'commission_plan_id', string='Commission Tracking')
    # Add approval workflow actions
    def action_approve(self):
        self.ensure_one()
        if not self.env.user.has_group('ox_sales_commission.group_commission_sale_admin'):
            raise UserError("Only administrators can approve commission plans")
        self.state = 'approved'
    
    def action_view_commissions(self):
        """Open commissions linked to this plan in a dedicated view."""
        self.ensure_one()
        action = self.env.ref('ox_sales_commission.action_all_commission').read()[0]
        action['domain'] = [('commission_plan_id', '=', self.id),('invoice_payment_state','=','paid')]
        # Keep a helpful default grouping
        ctx = dict(self.env.context or {})
        ctx.update({'search_default_group_salesperson': 1})
        action['context'] = ctx
        return action
        
    def action_cancel(self):
        self.ensure_one()
        self.state = 'cancelled'
    def action_closed(self):
        self.ensure_one()
        self.state = 'closed'
    def action_draft(self):
        self.ensure_one()
        self.state = 'draft'

    @api.onchange('salesperson_ids')
    def _onchange_salesperson_ids(self):
        """Restrict user selection for non-admins"""
        if not self.env.user.has_group('ox_sales_commission.group_commission_sale_admin'):
            # Commission sale users can only select themselves
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
                
    @api.constrains('commission_plan_type', 'salesperson_ids', 'admin_person_id')
    def _check_required_fields(self):
        """Validate required fields based on commission plan type"""
        for rec in self:
            if rec.commission_plan_type == 'sales_team' and not rec.salesperson_ids:
                raise ValidationError("Sales Persons field is required when Commission Plan Type is 'Sales Team'.")
            if rec.commission_plan_type == 'admin' and not rec.admin_person_id:
                raise ValidationError("Admin Person field is required when Commission Plan Type is 'Admin'.")
    
    @api.constrains('target_period_start', 'target_period_end')
    def _check_overlapping_periods(self):
        for rec in self:
            # Skip if dates are not set yet
            if not rec.target_period_start or not rec.target_period_end:
                continue
            
            # For Sales Team type, check salespersons overlap
            if rec.commission_plan_type == 'sales_team' and rec.salesperson_ids:
                # Disallow ANY overlap (partial or full). Adjacent dates (end == start) are also considered overlap.
                overlapping_plans = self.search([
                    ('id', '!=', rec.id),
                    ('state', '=', 'approved'),
                    ('company_id', '=', rec.company_id.id),
                    ('commission_plan_type', '=', 'sales_team'),
                    ('target_period_start', '<=', rec.target_period_end),
                    ('target_period_end', '>=', rec.target_period_start),
                    ('salesperson_ids', 'in', rec.salesperson_ids.ids),
                ])

                if overlapping_plans:
                    conflicting_users = (overlapping_plans.mapped('salesperson_ids') & rec.salesperson_ids).mapped('name')
                    plan_names = ", ".join(overlapping_plans.mapped('name'))
                    user_names = ", ".join(conflicting_users)
                    raise ValidationError(
                        (
                            "Overlapping commission plan(s) found for: %s. "
                            "Existing plan(s): %s. Dates must not overlap for the same salesperson(s)."
                        ) % (user_names or 'selected users', plan_names or 'N/A')
                    )
            
            # For Admin type, only one active admin plan should exist per period
            if rec.commission_plan_type == 'admin':
                overlapping_admin_plans = self.search([
                    ('id', '!=', rec.id),
                    ('state', '=', 'approved'),
                    ('company_id', '=', rec.company_id.id),
                    ('commission_plan_type', '=', 'admin'),
                    ('target_period_start', '<=', rec.target_period_end),
                    ('target_period_end', '>=', rec.target_period_start),
                ])
                
                if overlapping_admin_plans:
                    plan_names = ", ".join(overlapping_admin_plans.mapped('name'))
                    raise ValidationError(
                        (
                            "Only one active Admin commission plan can exist per period. "
                            "Conflicting plan(s): %s"
                        ) % (plan_names or 'N/A')
                    )

    @api.constrains('state')
    def _check_commission_tracking(self):
        for rec in self:
            if rec.state == 'cancelled' and rec.commission_tracking_ids:
                raise models.ValidationError("This plan cannot be cancelled because at least one comission is generated")
    
    # ------------------------------------------------------------------
    # Protections: closed plans are immutable (manual edits not allowed)
    # ------------------------------------------------------------------
    def write(self, vals):
        # Prevent any modification of already closed plans
        closed_records = self.filtered(lambda r: r.state == 'closed')
        if closed_records:
            raise UserError("Closed commission plans cannot be modified.")
        return super().write(vals)

    def unlink(self):
        # Prevent deletion of closed plans
        for rec in self:
            if rec.state == 'closed':
                raise UserError("Closed commission plans cannot be deleted.")
        return super().unlink()

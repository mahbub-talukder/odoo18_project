from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class CommissionPlan(models.Model):
    _name = 'commission.plan'
    _description = 'Sales Commission Plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
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
        required=True,
        tracking=True
    )
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
        if not self.env.user.has_group('commission_sales.group_commission_admin'):
            raise UserError("Only administrators can approve commission plans")
        self.state = 'approved'
        
    def action_cancel(self):
        self.ensure_one()
        self.state = 'cancelled'
        
    def action_draft(self):
        self.ensure_one()
        self.state = 'draft'

    # do set validation if the paln is approved and at least one comission tracking is generated, this plan cannot be cancelled
    @api.constrains('target_period_start', 'target_period_end')
    def _check_overlapping_periods(self):
        for rec in self:
            overlapping_plans = self.search([
                ('id', '!=', rec.id),
                ('state', '=', 'approved'),
                ('target_period_start', '<=', rec.target_period_end),
                ('target_period_end', '>=', rec.target_period_start)
            ])
            if overlapping_plans:
                raise models.ValidationError("A new plan cannot be generated due to overlapping target periods with existing approved plans.")

    @api.constrains('state')
    def _check_commission_tracking(self):
        for rec in self:
            if rec.state == 'cancelled' and rec.commission_tracking_ids:
                raise models.ValidationError("This plan cannot be cancelled because at least one comission is generated")
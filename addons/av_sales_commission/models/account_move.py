from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    commission_plan_id = fields.Many2one('sales.commission', string="Commission Plan", readonly=True)
    report_id = fields.One2many('sales.commission.report', 'bill_id', string="Commission Report", readonly=True)
    
    def action_view_commission_plan(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Commission Plan',
            'res_model': 'sales.commission',
            'res_id': self.commission_plan_id.id,
            'view_mode': 'form',
            'target': 'current',
        } 
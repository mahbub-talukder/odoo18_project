
from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    commission_tracking_ids = fields.One2many('commission.tracking', 'sale_order_id', 
                                               string='Commission Tracking')
    
    def action_confirm(self):
        res = super().action_confirm()
        self._create_commission_tracking()
        return res
    
    def _create_commission_tracking(self):
        for order in self:
            if not order.user_id:
                continue
                
            # Find active commission plan for this salesperson
            commission_plan = self.env['commission.plan'].search([
                ('salesperson_ids', 'in', order.user_id.id),
                ('state', '=', 'approved'),
                ('target_period_start', '<=', order.date_order.date()),
                ('target_period_end', '>=', order.date_order.date())
            ], limit=1)
            
            if not commission_plan:
                continue
            
            # Check if first order
            is_first = self._is_customer_first_order(order.partner_id.id, order.user_id.id)
            is_salesperson_first_order = self._is_salesperson_first_order(order.user_id.id)
            
            commission_vals = {
                'sale_order_id': order.id,
                'salesperson_id': order.user_id.id,
                'commission_plan_id': commission_plan.id,
                'order_amount': order.amount_total,
                'commission_type': 'first_order' if is_first else 'residual',
                'commission_percentage': commission_plan.first_order_commission if is_first else commission_plan.residual_commission,
            }
            
            self.env['commission.tracking'].create(commission_vals)
    
    def _is_customer_first_order(self, partner_id, user_id):
        previous_orders = self.search_count([
            ('partner_id', '=', partner_id),
            ('user_id', '=', user_id),
            ('state', 'in', ['sale', 'done']),
            ('id', '!=', self.id)
        ])
        return previous_orders == 0
    
    def _is_salesperson_first_order(self, user_id):
        previous_orders = self.search_count([
            ('user_id', '=', user_id),
            ('state', 'in', ['sale', 'done']),
            ('id', '!=', self.id)
        ])
        return previous_orders == 0
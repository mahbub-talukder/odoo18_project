
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
            # First, check for active Admin commission plans
            # Admin plans apply to ALL sales orders regardless of salesperson
            admin_plan = self.env['commission.plan'].search([
                ('commission_plan_type', '=', 'admin'),
                ('state', '=', 'approved'),
                ('target_period_start', '<=', order.date_order.date()),
                ('target_period_end', '>=', order.date_order.date())
            ], limit=1)
            
            if admin_plan:
                # Create commission for admin person
                # Admin commissions use a flat rate (first_order_commission) or can be a fixed percentage
                admin_commission_vals = {
                    'sale_order_id': order.id,
                    'salesperson_id': admin_plan.admin_person_id.id,
                    'commission_plan_id': admin_plan.id,
                    'order_amount': order.amount_total,
                    'commission_type': 'admin',
                    # For admin, use first_order_commission as the standard rate
                    'commission_percentage': admin_plan.first_order_commission,
                }
                
                # Create admin commission tracking with elevated rights
                self.env['commission.tracking'].sudo().create(admin_commission_vals)
            
            # Then, check for Sales Team commission plans (original logic)
            if not order.user_id:
                continue
                
            # Find active Sales Team commission plan for this salesperson
            sales_team_plan = self.env['commission.plan'].search([
                ('commission_plan_type', '=', 'sales_team'),
                ('salesperson_ids', 'in', order.user_id.id),
                ('state', '=', 'approved'),
                ('target_period_start', '<=', order.date_order.date()),
                ('target_period_end', '>=', order.date_order.date())
            ], limit=1)
            
            if not sales_team_plan:
                continue
            
            # Check if first order for this salesperson and customer
            is_first = self._is_customer_first_order(order.partner_id.id, order.user_id.id)
            
            commission_type = 'first_order' if is_first else 'residual'
                
            commission_vals = {
                'sale_order_id': order.id,
                'salesperson_id': order.user_id.id,
                'commission_plan_id': sales_team_plan.id,
                'order_amount': order.amount_total,
                'commission_type': commission_type,
                'commission_percentage': sales_team_plan.first_order_commission if is_first else sales_team_plan.residual_commission,
            }
            
            # Create commission tracking with elevated rights to avoid access errors
            # for regular sales users during confirmation.
            self.env['commission.tracking'].sudo().create(commission_vals)
    
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
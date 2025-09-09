from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def _post(self, soft=True):
        """Override to link invoices to commission tracking when posted"""
        res = super()._post(soft=soft)
        
        for move in self:
            if move.move_type == 'out_invoice' and move.invoice_origin:
                # Find commission tracking records for this sale order
                sale_order = self.env['sale.order'].search([
                    ('name', '=', move.invoice_origin)
                ], limit=1)
                
                if sale_order:
                    commission_records = self.env['commission.tracking'].search([
                        ('sale_order_id', '=', sale_order.id),
                        ('invoice_id', '=', False)
                    ])
                    
                    for commission in commission_records:
                        commission.invoice_id = move.id
        
        return res

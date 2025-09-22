from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
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
                    commission_records = self.env['commission.tracking'].sudo().search([
                        ('sale_order_id', '=', sale_order.id),
                        ('invoice_id', '=', False)
                    ])
                    
                    for commission in commission_records:
                        commission.sudo().invoice_id = move.id
            
            # Handle vendor bill payment for commission tracking
            elif move.move_type == 'in_invoice' and move.payment_state == 'paid':
                # Find commission tracking records linked to this vendor bill
                commission_records = self.env['commission.tracking'].sudo().search([
                    ('vendor_bill_id', '=', move.id),
                    ('is_paid', '=', False)
                ])
                
                for commission in commission_records:
                    commission.sudo().is_paid = True
        
        return res
    
    def write(self, vals):
        """Override write to handle payment state changes for vendor bills and customer invoices"""
        res = super().write(vals)
        _logger.info(f"res: {res}, vals: {vals}")

        # find the move where vendor bill id is euq
        # Check if payment_state is being updated

        for move in self:
            _logger.info(f"\n======debug move.state: {move.state},move.payment_state: {move.payment_state},move.move_type: {move.move_type},invoice_origin: {move.invoice_origin}\n")
            



            if move.move_type == 'in_invoice' and move.payment_state == 'paid':
                
                # Find commission tracking records linked to this vendor bill
                commission_records = self.env['commission.tracking'].search([
                    ('vendor_bill_id', '=', move.id),
                    ('is_paid', '=', False)
                ])
                
                for commission in commission_records:
                    commission.is_paid = True
                    
            elif move.move_type == 'in_invoice' and move.payment_state in ['not_paid', 'partial']:
                # Handle case when payment is reversed or partial
                commission_records = self.env['commission.tracking'].sudo().search([
                    ('vendor_bill_id', '=', move.id),
                    ('is_paid', '=', True)
                ])
                
                for commission in commission_records:
                    commission.sudo().is_paid = False

            # Track invoice paid date for customer invoices
            if move.move_type == 'out_invoice' and 'payment_state' in vals:
                if move.payment_state == 'paid':
                    commission_records = self.env['commission.tracking'].sudo().search([
                        ('invoice_id', '=', move.id)
                    ])
                    for commission in commission_records:
                        if not commission.invoice_paid_date:
                            commission.invoice_paid_date = fields.Date.context_today(self)
                elif move.payment_state in ['not_paid', 'partial']:
                    commission_records = self.env['commission.tracking'].sudo().search([
                        ('invoice_id', '=', move.id)
                    ])
                    for commission in commission_records:
                        commission.invoice_paid_date = False
        
        return res

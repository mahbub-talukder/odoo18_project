# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = "account.move"
    
    @api.model
    def create(self, vals):
        """
        Override to capture invoice creation and check for pending payments to reconcile.
        This handles manually created invoices.
        """
        invoice = super(AccountMove, self).create(vals)
        
        # Only process customer invoices
        if invoice.move_type != 'out_invoice':
            return invoice
            
        # Find sale order(s) related to this invoice
        sale_orders = self.env['sale.order'].sudo().search([
            ('name', '=', invoice.invoice_origin)
        ])
        
        # Check if any of these orders have standalone payments that need reconciliation
        for order in sale_orders:
            if order.standalone_payment_ids:
                # If invoice is created in posted state, reconcile immediately
                if invoice.state == 'posted':
                    for payment in order.standalone_payment_ids:
                        self._reconcile_standalone_payment(payment, invoice)
        
        return invoice
    
    def action_post(self):
        """
        Override to reconcile any pending payments when an invoice is posted.
        This handles the case when invoices are manually validated.
        """
        result = super(AccountMove, self).action_post()
        
        # Only process customer invoices
        for invoice in self.filtered(lambda m: m.move_type == 'out_invoice'):
            # Find sale order(s) related to this invoice
            sale_orders = self.env['sale.order'].sudo().search([
                ('name', '=', invoice.invoice_origin)
            ])
            
            # Check if any of these orders have standalone payments that need reconciliation
            for order in sale_orders:
                if order.standalone_payment_ids:
                    for payment in order.standalone_payment_ids:
                        self._reconcile_standalone_payment(payment, invoice)
        
        return result
    
    def _reconcile_standalone_payment(self, payment, invoice):
        """
        Enhanced reconciliation method to ensure invoices are properly marked as paid.
        
        :param payment: account.payment record
        :param invoice: account.move record (invoice)
        :return: True if reconciliation successful, False otherwise
        """
        try:
            _logger.info("Attempting to reconcile payment %s with invoice %s", payment.id, invoice.id)
            
            # First try the standard method
            sale_order = self.env['sale.order'].sudo()
            sale_order.reconcile_payment_ept(payment, invoice)
            
            # Check if invoice is marked as paid
            invoice.invalidate_recordset(['payment_state'])
            if invoice.payment_state not in ['paid', 'in_payment']:
                _logger.info("Standard reconciliation didn't mark invoice as paid. Trying direct reconciliation.")
                # Get receivable lines
                invoice_line = invoice.line_ids.filtered(
                    lambda line: line.account_id.account_type == 'asset_receivable' and not line.reconciled
                )
                payment_line = payment.move_id.line_ids.filtered(
                    lambda line: line.account_id.account_type == 'asset_receivable' and not line.reconciled
                )
                
                if invoice_line and payment_line:
                    # Reconcile the lines directly
                    (payment_line + invoice_line).reconcile()
                    invoice.invalidate_recordset(['payment_state'])
                    _logger.info("Invoice payment state after direct reconciliation: %s", invoice.payment_state)
                else:
                    _logger.warning("Cannot find appropriate receivable lines for direct reconciliation")
            
            return True
        except Exception as e:
            _logger.exception("Error reconciling payment with invoice: %s", str(e))
            return False 
import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        """Override to add automation when a payment is confirmed"""
        res = super(AccountPayment, self).action_post()
        
        # Trigger the automation only for inbound payments
        for payment in self.filtered(lambda p: p.partner_id and p.payment_type == 'inbound'):
            self.env['unified.sales.automation'].sudo().process_payment_automation(payment)
        
        return res

class SalesAutomation(models.Model):
    _name = 'unified.sales.automation'
    _description = 'Sales Process Automation'

    @api.model
    def process_payment_automation(self, payment):
        """Process automation when a payment is confirmed"""
        partner = payment.partner_id
        if not partner:
            return
        
        _logger.info("Processing payment automation for partner %s", partner.name)
        
        # Find the latest quotation in draft state for this partner (LIFO)
        quotation = self.env['sale.order'].search([
            ('partner_id', '=', partner.id),
            ('state', '=', 'draft')
        ], order='create_date DESC', limit=1)
        
        if not quotation:
            _logger.info("No draft quotation found for partner %s", partner.name)
            return
        
        try:
            # 1. Confirm the quotation
            _logger.info("Confirming quotation %s", quotation.name)
            quotation.action_confirm()
            
            # 2. Create and validate invoice
            _logger.info("Creating invoice for sales order %s", quotation.name)
            invoice = self._create_invoice(quotation)
            
            # 3. Reconcile payment with invoice
            if invoice and payment:
                self._reconcile_payment_with_invoice(payment, invoice)
                
            return True
        except Exception as e:
            _logger.error("Error in payment automation: %s", str(e))
            return False
    
    def _create_invoice(self, sale_order):
        """Create and validate invoice for the sale order"""
        if not sale_order.invoice_ids:
            context = {'active_model': 'sale.order', 'active_ids': [sale_order.id]}
            # Create the invoice
            invoice_wizard = self.env['sale.advance.payment.inv'].with_context(context).create({
                'advance_payment_method': 'delivered'
            })
            invoice_wizard.create_invoices()
        
        # Get the created invoice
        invoice = sale_order.invoice_ids.sorted(lambda i: i.id, reverse=True)[0]
        
        # Validate the invoice
        invoice.action_post()
        
        return invoice
    
    def _reconcile_payment_with_invoice(self, payment, invoice):
        """Reconcile the payment with the invoice"""
        _logger.info("Attempting to reconcile payment %s with invoice %s", payment.name, invoice.name)
        
        if invoice.payment_state in ['paid', 'in_payment']:
            _logger.info("Invoice %s is already paid or in payment", invoice.name)
            return True
        
        if not payment.move_id:
            _logger.error("Payment %s has no move_id", payment.name)
            return False
        
        # Get the move lines
        invoice_line = invoice.line_ids.filtered(
            lambda line: line.account_id.account_type in ('asset_receivable', 'liability_payable')
        )
        payment_line = payment.move_id.line_ids.filtered(
            lambda line: line.account_id.account_type in ('asset_receivable', 'liability_payable')
        )
        
        if not invoice_line or not payment_line:
            _logger.warning("Cannot find appropriate journal items for reconciliation")
            return False
        
        # Prepare lines for reconciliation
        lines_to_reconcile = invoice_line + payment_line
        
        # Reconcile
        lines_to_reconcile.reconcile()
        
        _logger.info("Successfully reconciled payment with invoice")
        return True 
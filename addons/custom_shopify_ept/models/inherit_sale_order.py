# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError
logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Field to store standalone payments for orders that don't have invoices yet
    standalone_payment_ids = fields.Many2many('account.payment', string='Standalone Payments',
                                            help='Payments created before invoice generation')
    
    # Field to store the workflow that was applied
    applied_workflow_id = fields.Many2one('sale.workflow.process.ept', 
                                          string='Applied Workflow')

    def validate_and_paid_invoices_ept(self, work_flow_process_record):
        """
        Custom implementation to handle special workflow cases.
        
        Case 1: validate_order and register_payment are checked (but not create_invoice)
        - Order is confirmed
        - Payment is created (without invoice) for the customer
        - No invoice is generated
        - Payment will be automatically reconciled with future invoices
        
        Case 2: All three are checked (validate_order, create_invoice, register_payment)
        - Regular flow is followed (order confirmed, invoice created/validated, payment registered)
        - Payment is created regardless of Shopify payment info
        
        @param work_flow_process_record: Record of auto invoice workflow.
        """
        self.ensure_one()
        
        # Check if this is a Shopify order and if we should use the base implementation
        if hasattr(self, 'shopify_instance_id') and not self.shopify_instance_id:
            return super(SaleOrder, self).validate_and_paid_invoices_ept(work_flow_process_record)
            
        # Case 2: Regular flow - all three options are checked
        if work_flow_process_record.validate_order and work_flow_process_record.create_invoice and work_flow_process_record.register_payment:
            return super(SaleOrder, self).validate_and_paid_invoices_ept(work_flow_process_record)
        
        # Case 1: Only validate_order and register_payment are checked (but not create_invoice)
        if work_flow_process_record.validate_order and work_flow_process_record.register_payment and not work_flow_process_record.create_invoice:
            # Confirm the order if it's not confirmed yet
            if self.state not in ['sale', 'done', 'cancel']:
                self.action_confirm()
                
            # Create a standalone payment for the order total
            self._create_standalone_payment(work_flow_process_record)
            
            # Store the workflow that was applied
            self.write({'applied_workflow_id': work_flow_process_record.id})
            return True
            
        # For all other cases, use default behavior
        return super(SaleOrder, self).validate_and_paid_invoices_ept(work_flow_process_record)
    
    def _create_standalone_payment(self, work_flow_process_record):
        """
        Create a standalone payment for the order total, without an invoice.
        This payment will be stored and can be reconciled later when invoices are created.
        Uses sudo() to ensure proper access rights for payment creation.
        
        @param work_flow_process_record: Record of workflow configuration
        @return: account.payment record
        """
        self.ensure_one()
        account_payment_obj = self.env['account.payment'].sudo()
        
        # Check if payment already exists
        if self.standalone_payment_ids:
            return self.standalone_payment_ids[0]
            
        # Prepare payment values
        vals = {
            'journal_id': work_flow_process_record.journal_id.id,
            'memo': f'Payment for {self.name}',
            'currency_id': self.currency_id.id,
            'payment_type': 'inbound',
            'date': fields.Date.context_today(self),
            'partner_id': self.partner_id.commercial_partner_id.id,
            'amount': self.amount_total,
            'payment_method_id': work_flow_process_record.inbound_payment_method_id.id,
            'partner_type': 'customer',
            'write_off_line_vals': []
        }
        
        # Create and post the payment with sudo to bypass security restrictions
        payment_id = account_payment_obj.create(vals)
        payment_id.sudo().action_post()
        
        # Store the payment reference in the sale order
        self.write({'standalone_payment_ids': [(4, payment_id.id)]})
        
        return payment_id
    
    def action_confirm(self):
        """
        Override action_confirm to apply workflow logic to manually created quotations.
        This ensures the same behavior for both Shopify imports and manual quotations.
        Uses sudo() for operations that require elevated permissions.
        """
        result = super(SaleOrder, self).action_confirm()
        
        # After confirming the order, check if we need to apply custom workflow logic
        # This applies to manually created quotations
        for order in self:
            # Skip orders that already have an applied workflow (to avoid duplicates)
            if order.applied_workflow_id:
                continue
                
            # Find eligible workflows - use sudo to ensure we can see all workflows
            # workflows = self.env['sale.workflow.process.ept'].sudo().search([
            #     ('validate_order', '=', True),
            #     ('register_payment', '=', True),
            #     ('create_invoice', '=', False)
            # ], limit=1)

            work_flow_process_record = order.auto_workflow_process_id
            if not work_flow_process_record:
                raise UserError(_("No workflow found for order %s,First do select the workflow under others info tab in sale order", order.name))
            

            try:
                # Create standalone payment based on the first eligible workflow
                # Case 1: Only validate_order and register_payment are checked (but not create_invoice)
                if work_flow_process_record.validate_order and work_flow_process_record.register_payment and not work_flow_process_record.create_invoice:
                        
                    # Create a standalone payment for the order total
                    self._create_standalone_payment(work_flow_process_record)
                    
                    # Store the workflow that was applied
                    self.write({'applied_workflow_id': work_flow_process_record.id})
            except Exception as e:
                # Log error but don't prevent order confirmation
                self.env.user.notify_warning(
                    message=f"Could not create automatic payment: {str(e)}",
                    title="Payment Creation Error", 
                    sticky=True
                )
                
        return result
    
    def action_invoice_create(self, grouped=False, final=False):
        """
        Override to reconcile standalone payments with newly created invoices.
        
        @param grouped: Boolean that determines if we group by partner
        @param final: Boolean that determines if this is a final invoice
        @return: invoice ids created
        """
        invoice_ids = super(SaleOrder, self).action_invoice_create(grouped, final)
        
        # If there are standalone payments, reconcile them with the new invoices
        if self.standalone_payment_ids:
            invoices = self.env['account.move'].browse(invoice_ids)
            for payment in self.standalone_payment_ids:
                for invoice in invoices:
                    self.env['sale.order'].sudo().reconcile_payment_ept(payment, invoice)
                    
        return invoice_ids
    
    def _create_invoices(self, grouped=False, final=False, date=None):
        """
        Override to reconcile standalone payments with newly created invoices.
        This is for Odoo 18 which uses _create_invoices instead of action_invoice_create
        
        @param grouped: Boolean that determines if we group by partner
        @param final: Boolean that determines if this is a final invoice
        @param date: Optional invoice date
        @return: invoices created
        """
        invoices = super(SaleOrder, self)._create_invoices(grouped, final, date)
        
        # If there are standalone payments, reconcile them with the new invoices
        if self.standalone_payment_ids:
            for payment in self.standalone_payment_ids:
                for invoice in invoices:
                    if invoice.state == 'draft':
                        invoice.sudo().action_post()
                    self.env['sale.order'].sudo().reconcile_payment_ept(payment, invoice)
                    
        return invoices 
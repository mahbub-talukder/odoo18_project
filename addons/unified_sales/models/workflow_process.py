# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class SaleWorkflowProcess(models.Model):
    _name = "unified.sales.workflow.process"
    # _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "sale workflow process"

    @api.model
    def _default_journal(self):
        """
        Define this method for find sales journal based on passed company in context or user's company.
        :return: account.journal()
        """
        account_journal_obj = self.env['account.journal']
        company_id = self._context.get('company_id', self.env.company.id)
        domain = [('type', '=', "sale"), ('company_id', '=', company_id)]
        return account_journal_obj.search(domain, limit=1)

    name = fields.Char(size=64)
    validate_order = fields.Boolean("Confirm Quotation", default=False,
                                    help="If it's checked, Order will be Validated.", tracking=True)
    create_invoice = fields.Boolean('Create & Validate Invoice', default=False,
                                    help="If it's checked, Invoice for Order will be Created and Posted.",
                                    tracking=True)
    register_payment = fields.Boolean(default=False, help="If it's checked, Payment will be registered for Invoice.",
                                      tracking=True)
    invoice_date_is_order_date = fields.Boolean('Force Accounting Date',
                                                help="if it is checked then, the account journal entry will be "
                                                     "generated based on Order date and if unchecked then, "
                                                     "the account journal entry will be generated based on Invoice Date",
                                                tracking=True)
    journal_id = fields.Many2one('account.journal', string='Payment Journal', 
                                 tracking=True)
    sale_journal_id = fields.Many2one('account.journal', string='Sales Journal', default=_default_journal,
                                      tracking=True)
    picking_policy = fields.Selection([('direct', 'Deliver each product when available'),
                                       ('one', 'Deliver all products at once')], string='Shipping Policy',
                                      default="one", tracking=True)
    inbound_payment_method_id = fields.Many2one('account.payment.method', string="Debit Method",
                                                domain=[('payment_type', '=', 'inbound')],
                                                help="Means of payment for collecting money. Odoo modules offer various"
                                                     "payments handling facilities, but you can always use the 'Manual'"
                                                     "payment method in order to manage payments outside of the"
                                                     "software.", tracking=True)
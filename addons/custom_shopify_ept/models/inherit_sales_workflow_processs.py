# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, api, fields


class SaleWorkflowProcess(models.Model):
    _inherit = "sale.workflow.process.ept"
    _description = "Sale Workflow Process"

    # Override just this field to update the help text
    register_payment = fields.Boolean(
        default=False, 
        help="If it's checked, Payment will be registered for Invoice or "
             "created as a standalone payment if no invoice exists.",
        tracking=True
    )

    # Removing the dependency between register_payment and create_invoice
    # In the default implementation, if create_invoice is unchecked, register_payment is also unchecked
    # We are removing this restriction to allow register_payment without create_invoice
    @api.onchange("create_invoice")
    def onchange_create_invoice(self):
        """
        Removed the dependency between create_invoice and register_payment.
        Now register_payment can be used even when create_invoice is not set.
        """
        # We intentionally leave this method empty to override the behavior
        # from the base module that would enforce the dependency
        pass
from odoo import fields, models, api, _

class AdvanceType(models.Model):
	_name = "advance.type"
	_description = "Tipo de anticipo"

	name = fields.Char(string="Name", required=True)
	account_id = fields.Many2one('account.account', string="Cuenta de anticipo", required=True, domain=[('account_type','in',('asset_receivable', 'liability_payable'))])
	internal_type = fields.Selection(related='account_id.account_type', string="Internal Type", store=True, readonly=True)
	company_id = fields.Many2one('res.company', related='account_id.company_id', string='Company', store=True, readonly=True)

class Account(models.Model):
    _inherit = 'account.account'

    used_for_advance_payment = fields.Boolean('Cuenta Anticipo')

    @api.onchange('used_for_advance_payment')
    def onchange_used_for_advance_payment(self):
        if self.used_for_advance_payment:
            self.reconcile = self.used_for_advance_payment

    def write(self, vals):
        if vals.get('used_for_advance_payment'):
            vals['reconcile'] = True
        return super(Account, self).write(vals)

class Company(models.Model):
    _inherit = 'res.company'

    advance_payment_journal_id = fields.Many2one(
        'account.journal',
        string="Diario de pagos anticipados",
        help="Default advance payment journal for the current user's company."
    )

from odoo import fields, models, api, _

class AdvanceType(models.Model):
	_name = "advance.type"
	_description = "Tipo de anticipo"

	name = fields.Char(string="Name", required=True)
	account_id = fields.Many2one('account.account', string="Cuenta de anticipo", required=True, domain=[('account_type','in',('asset_receivable', 'liability_payable'))])
	internal_type = fields.Selection(related='account_id.account_type', string="Internal Type", store=True, readonly=True)
	company_id = fields.Many2one('res.company', string='Company', compute='_compute_company_id', store=True, readonly=True)

	@api.depends('account_id')
	def _compute_company_id(self):
		for record in self:
			# In Odoo 18, account.account has company_ids (Many2many) instead of company_id (Many2one)
			if record.account_id and record.account_id.company_ids:
				# Take the first company or current user's company if available
				user_company = self.env.company
				if user_company in record.account_id.company_ids:
					record.company_id = user_company
				else:
					record.company_id = record.account_id.company_ids[0]
			else:
				record.company_id = False

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

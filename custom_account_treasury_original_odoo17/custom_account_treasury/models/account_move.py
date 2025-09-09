from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, format_date, get_lang
import logging
import json
from json import dumps
from odoo.tools import float_is_zero, UserError, datetime
from contextlib import ExitStack, contextmanager
_logger = logging.getLogger(__name__)

MAP_INVOICE_TYPE_PARTNER_TYPE = {
    'out_invoice': 'customer',
    'out_refund': 'customer',
    'out_receipt': 'customer',
    'in_invoice': 'supplier',
    'in_refund': 'supplier',
    'in_receipt': 'supplier',
}

# class AccountPaymentRegister(models.TransientModel):
# 	_inherit='account.payment.register'

# 	account_id = fields.Many2one(
# 		comodel_name='account.account',
# 		string='Cuenta de origen',
# 		store=True, readonly=False,
# 		domain="[('deprecated', '=', False), ('company_id', '=', company_id)]",
# 		check_company=True)
# 	destination_account_id = fields.Many2one(
# 		comodel_name='account.account',
# 		string='Destination Account',
# 		store=True, readonly=False,
# 		domain="[('account_type', 'in', ('asset_receivable', 'liability_payable')), ('company_id', '=', company_id)]",
# 		check_company=True)
# 	change_destination_account = fields.Char(string="cambio de cuenta destino")

# 	# def _create_payment_vals_from_wizard(self):
# 	# 	payment_vals = super(AccountPaymentRegister, self)._create_payment_vals_from_wizard()
# 	# 	if self.account_id:
# 	# 		payment_vals['account_id'] = self.account_id.id
# 	# 	if self.destination_account_id:
# 	# 		payment_vals['destination_account_id'] = self.destination_account_id.id
# 	# 	return payment_vals

class AccountMove(models.Model):
	_inherit = "account.move"

	pay_id = fields.Many2one(comodel_name='account.payment',string='Pago',required=False)
	advance_payment_ids = fields.Many2many('account.move.line', 'account_move_advance_payment_rel', 'move_id', 'advance_payment_line_id', string='Anticipos')
	advance_payment_total = fields.Monetary(compute='_compute_advance_payment_total', string='Total Anticipo', currency_field='currency_id')
	advance_payment_residual = fields.Monetary(compute='_compute_advance_payment_total', string='Pagos anticipados restantes', currency_field='currency_id')
	advance_payment_count = fields.Integer(compute='_compute_advance_payments',  string='advance payment?')
	has_advance_payment = fields.Boolean(compute='_has_advance_payment', 
	string='Has advance payment?')

	@api.depends('line_ids','advance_payment_count')
	def _compute_advance_payments(self):
		for invoice in self:
			invoice.advance_payment_count = len(invoice.advance_payment_ids)
	
	def js_remove_outstanding_partial(self, partial_id):
		self.ensure_one()
		partial = self.env['account.partial.reconcile'].browse(partial_id)
		lines = partial.debit_move_id | partial.credit_move_id
		lines |= lines.mapped('move_id.line_ids')

		result = super().js_remove_outstanding_partial(partial_id)

		# Remove advance payment journal entries
		for advance_payment_move in lines.filtered(lambda line: line.account_id.used_for_advance_payment).move_id:
			advance_payment_move.button_draft()
			advance_payment_move.button_cancel()
			advance_payment_move.with_context(force_delete=True).unlink()

	def _has_advance_payment(self):
		for invoice in self:
			move = self.env['account.move.line'].search([
				('company_id', '=', self.company_id.id),
				('account_id.used_for_advance_payment', '=', True),
				('partner_id', '=', self.partner_id.id),
				('amount_residual', '!=', 0.0),
				('move_id.state', '=', 'posted'),
			])
			if move:
				invoice.has_advance_payment = True
			else:
				invoice.has_advance_payment = False

	@api.depends('advance_payment_ids')
	def _compute_advance_payment_total(self):
		for record in self:
			payment_residual = sum(record.advance_payment_ids.mapped('amount_residual'))
			record.advance_payment_total = payment_residual
			record.advance_payment_residual = payment_residual - record.amount_residual if payment_residual > record.amount_residual else 0.0

	@api.onchange('company_id', 'partner_id')
	def _onchange_advance_payment_ids(self):
		if self.company_id and self.partner_id:
			advance_payment_lines = self.env['account.move.line'].search([
				('company_id', '=', self.company_id.id),
				('account_id.used_for_advance_payment', '=', True),
				('partner_id', '=', self.partner_id.id),
				('amount_residual', '!=', 0.0),
				('move_id.state', '=', 'posted'),
			])
			self.advance_payment_ids = [(6, 0, advance_payment_lines.ids)]
		else:
			self.advance_payment_ids = [(5, 0, 0)]

	def apply_advance_payment(self):
		self.ensure_one()
		if not self.advance_payment_ids:
			if self.company_id and self.partner_id:
				advance_payment_lines = self.env['account.move.line'].search([
					('company_id', '=', self.company_id.id),
					('account_id.used_for_advance_payment', '=', True),
					('partner_id', '=', self.partner_id.id),
					('amount_residual', '!=', 0.0),  # Only negative residual value advance payments
					('move_id.state', '=', 'posted'),
					('advance_account', '=', False)
				])
				self.advance_payment_ids = [(6, 0, advance_payment_lines.ids)]
			else:
				self.advance_payment_ids = [(5, 0, 0)]
		
		partner = self.partner_id
		move_lines = self.line_ids.filtered(lambda r: not r.reconciled and r.account_id.account_type in ('asset_receivable', 'liability_payable'))
		date_invoice = self.invoice_date

		advance_payment_lines = self.advance_payment_ids
		advance_payment_accounts = advance_payment_lines.mapped('account_id')

		advance_payment_move_lines = []
		advance_payment_residual = self.advance_payment_total - self.advance_payment_residual
		currency_company = self.company_id.currency_id

		for line in advance_payment_lines:
			amount_residual = abs(line.amount_residual)
			currency = line.currency_id or currency_company
			currency_invoice = self.currency_id
			payment_date = line.date

			if currency_company != currency_invoice:
				advance_payment_residual = currency_invoice.with_context(date=payment_date).compute(advance_payment_residual, currency_company)

			balance_used = min(amount_residual, advance_payment_residual, self.amount_residual)
			if currency != currency_company and balance_used:
				if line.amount_currency:
					amount_currency = abs(line.amount_currency * (balance_used / amount_residual))
				else:
					amount_currency = balance_used
				balance_now = currency.with_context(date=date_invoice).compute(amount_currency, currency_company)
			else:
				balance_now = balance_used

			if self.move_type in ('out_invoice', 'in_refund'):
				credit = balance_used
				debit = 0.0
				advance_payment_residual -= credit
			else:
				debit = balance_used
				credit = 0.0
				advance_payment_residual -= debit

			account_id = line.account_id.id
			advance_payment_move_lines.append((0, 0, {
				'name': 'Anticipo: %s' % line.move_id.name,
				'date_maturity': fields.Date.today(),
				'account_id': account_id,
				'partner_id': partner.id,
				'debit': debit,
				'credit': credit,
				'advance_account': True,
			}))

			account_id = partner.property_account_receivable_id.id if self.move_type in ('out_invoice', 'in_refund') else partner.property_account_payable_id.id
			advance_payment_move_lines.append((0, 0, {
				'name': 'Anticipo: %s' % line.move_id.name,
				'date_maturity': fields.Date.today(),
				'account_id': account_id,
				'partner_id': partner.id,
				'debit': credit,
				'credit': debit,
				'advance_account': False,
			}))

		if advance_payment_move_lines:
			move = self.env['account.move'].with_context(skip_validation=True).create({
				'date': fields.Date.today(),
				'move_type': 'entry',
				'company_id': self.company_id.id,
				'journal_id': self.company_id.advance_payment_journal_id.id,
				'line_ids': advance_payment_move_lines,
			})
			move.action_post()
			for lines in move.line_ids:
				invoice_line = self.line_ids.filtered(lambda r: not r.reconciled and r.account_id.account_type in ('asset_receivable', 'liability_payable'))
				if (invoice_line.account_id == lines.account_id and
					invoice_line.partner_id == lines.partner_id and
					not invoice_line.reconciled):
					(lines + invoice_line).with_context(skip_account_move_synchronization=True).reconcile()
				if (lines.account_id == advance_payment_lines.account_id and 
					lines.partner_id == advance_payment_lines.partner_id and 
					not advance_payment_lines.reconciled):
					(lines + advance_payment_lines).with_context(skip_account_move_synchronization=True).reconcile()




class AccountMoveLine(models.Model):
	_inherit = "account.move.line"

	advance_account = fields.Boolean(string='Is advance payment?', default=False)
	line_pay = fields.Many2one('account.move.line', string='line Invoice')
	inv_id = fields.Many2one('account.move', string='Invoice')
	processed  = fields.Boolean(
		string='Procesado',
		required=False)

	@api.depends('ref', 'move_id')
	def name_get(self):
		super().name_get()
		result = []
		for line in self:
			if self._context.get('show_number', False):
				name = '%s - %s' %(line.move_id.name, abs(line.amount_residual_currency or line.amount_residual))
				result.append((line.id, name))
			elif line.ref:
				result.append((line.id, (line.move_id.name or '') + '(' + line.ref + ')'))
			else:
				result.append((line.id, line.move_id.name))
		return result

	@api.ondelete(at_uninstall=False)
	def _prevent_automatic_line_deletion(self):
		if not self.env.context.get('dynamic_unlink'):
			for line in self:
				#if line.display_type == 'tax' and line.move_id.line_ids.tax_ids:
				#	raise ValidationError(_(
				#		"You cannot delete a tax line as it would impact the tax report"
				#	))
				if line.display_type == 'payment_term':
					raise ValidationError(_(
						"You cannot delete a payable/receivable line as it would not be consistent "
						"with the payment terms"
					))


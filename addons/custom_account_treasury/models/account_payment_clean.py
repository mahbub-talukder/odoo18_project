from odoo import models, fields, api, _,Command
from odoo.exceptions import UserError, ValidationError
from odoo.tools import (
    date_utils,
    float_compare,
    float_is_zero,
    float_repr,
    format_amount,
    format_date,
    formatLang,
    frozendict,
    get_lang,
    is_html_empty,
    sql
)

import logging

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
	_inherit = 'account.payment'

	@api.depends('payment_line_ids.invoice_id')
	def _compute_domain_move_line(self):
		for pay in self:
			invoices = pay.mapped('payment_line_ids.invoice_id')
			pay.domain_move_lines = [(6,0,invoices.ids)]

	@api.depends('payment_line_ids.move_line_id')
	def _compute_domain_accountmove_line(self):
		for pay in self:
			invoices = pay.mapped('payment_line_ids.move_line_id')
			pay.domain_account_move_lines = [(6,0,invoices.ids)]


	move_diff_ids = fields.Many2many('account.move', 'account_move_payment_rel_ids', 'move_id', 'payment_id', copy=False)
	payment_line_ids = fields.One2many('account.payment.detail', 'payment_id', copy=False, string="Detalle de pago", help="detalle de pago")
	currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        compute='_compute_currency_id', store=True, readonly=False, precompute=True, default=lambda self: self.env.company.currency_id,
        help="The payment's currency.")
	destination_account_id = fields.Many2one(
		comodel_name='account.account',
		string='Destination Account',
		store=True, readonly=False,
		compute='_compute_destination_account_id',
		domain="[('account_type', 'in', ('asset_receivable', 'liability_payable')), '|', ('company_ids', '=', False), ('company_ids', 'in', company_id)]",
		check_company=True)
	change_destination_account = fields.Char(string="cambio de cuenta destino")

	invoice_cash_rounding_id = fields.Many2one(
		comodel_name='account.cash.rounding',
		string='Cash Rounding Method',
		readonly="state != 'draft'",
		help='Defines the smallest coinage of the currency that can be used to pay by cash.',
	)

	company_currency_id = fields.Many2one('res.currency', string="Moneda de la compañia",
		required=True, default=lambda self: self.env.company.currency_id)

	# === Buscar Documentos fields === #
	customer_invoice_ids = fields.Many2many("account.move", "customer_invoice_payment_rel", 'invoice_id', 'payment_id',
		string="Buscar Documentos Clientes", domain="[('state','!=','draft')]")
	supplier_invoice_ids = fields.Many2many("account.move", "supplier_invoice_payment_rel", 'invoice_id', 'payment_id',
		string="Buscar Documentos Proveedores", domain="[('state','!=','draft')]")
	account_move_payment_ids = fields.Many2many("account.move.line", "account_move_payment_rel", 'moe_line_id','payment_id',
		string="Buscar Otros Documentos", domain="[('amount_residual','!=', 0),('parent_state','!=','draft')]")
	
	invoice_id = fields.Many2one(
		comodel_name='account.move',
		string='Factura',
		required=False)

	# === Filtrar Documentos fields === #
	domain_account_move_lines = fields.Many2many("account.move.line", 'domain_account_move_line_pay_rel', string="restriccion de campos", compute="_compute_domain_accountmove_line")
	domain_move_lines = fields.Many2many("account.move", 'domain_move_line_pay_rel', string="restriccion de campos", compute="_compute_domain_move_line")


	# === advance fields === #
	advance_type_id = fields.Many2one('advance.type', string="Tipo de anticipo")
	advance = fields.Boolean('Anticipo', default=False)
	code_advance = fields.Char(string="Número de anticipo", copy=False)
	partner_type = fields.Selection(selection_add=[
		('employee', 'Empleado'),
	], ondelete={'employee': 'set default'})
	
	ref = fields.Char(string="Referencia", help="Payment reference")


	is_internal_transfer = fields.Boolean(compute='_compute_is_internal_transfer', store=True)

	@api.depends('move_id.line_ids.account_id')
	def _compute_is_internal_transfer(self):
		transfer_acc = self.env.company.transfer_account_id
		for rec in self:
			rec.is_internal_transfer = bool(transfer_acc and rec.move_id and  any(l.account_id == transfer_acc for l in rec.move_id.line_ids))

	# === writeoff fields === #
	writeoff_account_id = fields.Many2one('account.account', string="Cuenta de diferencia", copy=False,
		domain="[('deprecated', '=', False), '|', ('company_ids', '=', False), ('company_ids', 'in', company_id)]")
	writeoff_label = fields.Char(string='Journal Item Label', default='Diferencia',
		help='Change label of the counterpart that will hold the payment difference')
	payment_difference_line = fields.Monetary(string="Diferencia de pago",
		store=True, readonly=True,
		tracking=True)
	

	def open_reconcile_view(self):
		return self.move_id.line_ids.open_reconcile_view()

	@api.depends('journal_id')
	def _compute_currency_id(self):
		for pay in self:
			pay.currency_id = pay.journal_id.currency_id or pay.journal_id.company_id.currency_id or self.env.company.currency_id.id


	@api.onchange('payment_line_ids','payment_line_ids.tax_ids')
	def _onchange_matched_manual_ids(self, force_update = False):
		in_draft_mode = self != self._origin
		
		def need_update():
			amount = 0
			for line in self.payment_line_ids:
				if line.auto_tax_line:
					amount -= line.balance
					continue
				if line.tax_ids:
					balance_taxes_res = line.tax_ids._origin.compute_all(
						line.invoice_id.amount_untaxed  or line.payment_amount or line.balance,
						currency=line.currency_id,
						quantity=1,
						product=line.product_id,
						partner=line.partner_id,
						is_refund=False,
						handle_price_include=True,
					)
					for tax_res in balance_taxes_res.get("taxes"):
						amount += tax_res['amount']
			return amount 
		
		if not force_update and not need_update():
			return
		
		to_remove = self.env['account.payment.detail']		
		if self.payment_line_ids:
			for line in list(self.payment_line_ids):
				if line.auto_tax_line:
					to_remove += line
					continue
				if line.tax_ids:
					balance_taxes_res = line.tax_ids._origin.compute_all(
						line.invoice_id.amount_untaxed or line.payment_amount or line.balance,
						currency=line.currency_id,
						quantity=1,
						product=line.product_id,
						partner=line.partner_id,
						is_refund=False,
						handle_price_include=True,
					)
					for tax_res in balance_taxes_res.get("taxes"):
						create_method = in_draft_mode and line.new or line.create
						create_method({
							'payment_id' : self.id,
							'partner_id' : line.partner_id.id,
							'account_id' : tax_res['account_id'],
							'name' : tax_res['name'],
							'payment_amount' : tax_res['amount'],
							'tax_repartition_line_id' : tax_res['tax_repartition_line_id'],
							'tax_tag_ids' : tax_res['tag_ids'],
							'auto_tax_line' : True,
							'tax_line_id2' :tax_res['id'],
							'tax_base_amount' : line.invoice_id.amount_untaxed or line.payment_amount or line.balance,
							'tax_line_id' : line.id,
							})
			
			if in_draft_mode:
				self.payment_line_ids -=to_remove
			else:
				to_remove.unlink()

	def _prepare_move_line_default_vals(self, write_off_line_vals=None, force_balance=None):
		res = super(AccountPayment, self)._prepare_move_line_default_vals(write_off_line_vals,force_balance)
		new_aml_lines = []
		for line in self.payment_line_ids.filtered(lambda x: not float_is_zero(x.amount_currency, precision_digits=self.currency_id.decimal_places)):
			# Fully Paid line
			new_aml_lines.append(
				{
					'debit': line.debit,
					'credit': line.credit,
					'balance': line.debit - line.credit,
					'amount_currency': line.amount_currency if line.amount_currency != 0.0 else (line.debit - line.credit),
					'journal_id': self.journal_id.id,
					'account_id': line.account_id.id,
					'analytic_distribution': line.analytic_distribution or False,
					'tax_ids': [(6, 0, line.tax_ids.ids)],
					'tax_tag_ids': [(6, 0, line.tax_tag_ids.ids)],
					'tax_repartition_line_id': line.tax_repartition_line_id.id,
					'tax_base_amount': line.tax_base_amount,
					'inv_id': line.invoice_id.id,
					'line_pay': line.move_line_id.id,
					"date_maturity": self.date,
					"partner_id": line.partner_id.commercial_partner_id.id,
					"currency_id": line.payment_id.currency_id.id,
					"payment_id": self.id,
					#**line._get_counterpart_move_line_vals() 
				}
			)
		if len(res) >= 2 and new_aml_lines:
			res.pop(1)
			res += new_aml_lines
		return res




	
	# def _prepare_move_line_default_vals(self, write_off_line_vals=None): 
	# 	res = super(AccountPayment, self)._prepare_move_line_default_vals(write_off_line_vals)
	# 	#res[0].update({'is_main': True})
	# 	new_aml_lines = []
		
	# 	for line in self.payment_line_ids:
	# 		new_aml_lines.append(
	# 			{
	# 				'debit': line.debit,
	# 				'credit': line.credit,
	# 				'balance': line.debit - line.credit,
	# 				'amount_currency': line.amount_currency if line.amount_currency != 0.0 else (line.debit - line.credit),
	# 				'journal_id': self.journal_id.id,
	# 				'account_id': line.account_id.id,
	# 				'analytic_distribution': line.analytic_distribution or False,
	# 				'tax_ids': [(6, 0, line.tax_ids.ids)],
	# 				'tax_tag_ids': [(6, 0, line.tax_tag_ids.ids)],
	# 				'tax_repartition_line_id': line.tax_repartition_line_id.id,
	# 				'tax_base_amount': line.tax_base_amount,
	# 				'inv_id': line.invoice_id.id,
	# 				'line_pay': line.move_line_id.id,
	# 				"date_maturity": self.date,
	# 				"partner_id": line.partner_id.commercial_partner_id.id,
	# 				"currency_id": line.payment_id.currency_id.id,
	# 				"payment_id": self.id,
	# 				#'to_pay': line.to_pay,
	# 				#"payment_detail_id": line.id,
	# 				**line._get_counterpart_move_line_vals() 
	# 			}
	# 		)
		
	# 	if self.payment_line_ids:
	# 		res = new_aml_lines
			
	# 	return res

	@api.onchange('advance_type_id')
	def _onchange_advance_type_id(self):
		self._onchange_payment_type()

	@api.onchange('advance')
	def _onchange_advance(self):
		res = {}
		if not self.reconciled_invoice_ids:
			if self.payment_type == 'transfer':
				self.advance = False
				self.advance_type_id = False
			elif not self.advance:
				self.advance_type_id = False
		if self.advance:
			self.advance_type_id = False
			res['domain'] = {'advance_type_id': [('internal_type','=', self.payment_type == 'outbound' and 'asset_receivable' or 'liability_payable')]}
		return res

	def _get_moves_domain(self):
		domain = [
			("amount_residual", "!=", 0.0),
			("state", "=", "posted"),
			("company_id", "=", self.company_id.id),
			(
				"commercial_partner_id",
				"=",
				self.partner_id.commercial_partner_id.id,
			),
		]
		if self.partner_type == "supplier":
			if self.payment_type == "outbound":
				domain.append(("move_type", "in", ("in_invoice", "in_receipt")))
			if self.payment_type == "inbound":
				domain.append(("move_type", "=", "in_refund"))
		elif self.partner_type == "customer":
			if self.payment_type == "outbound":
				domain.append(("move_type", "=", "out_refund"))
			if self.payment_type == "inbound":
				domain.append(("move_type", "in", ("out_invoice", "out_receipt")))
		return domain

	def _filter_amls(self, amls):
		return amls.filtered(
			lambda x: x.partner_id.commercial_partner_id.id
			== self.partner_id.commercial_partner_id.id
			and x.amount_residual != 0
			and x.account_id.account_type in ("asset_receivable", "liability_payable")
		)

	def _hook_create_new_line(self, invoice, aml, amount_to_apply,amount_residual):
		line_model = self.env["account.payment.detail"]
		if amount_residual > 0:
			amount_to_apply *= -1
		self.ensure_one()
		return line_model.create(
			{
				"payment_id": self.id,
				"name": invoice.name + str(aml.ref),
				"move_id": invoice.id,
				"move_line_id": aml.id,
				"account_id": aml.account_id.id,
				"partner_id": self.partner_id.commercial_partner_id.id,
				"payment_amount": amount_to_apply,
			}
		)

	def action_propose_payment_distribution(self):
		move_model = self.env["account.move"]
		for rec in self:
			if self.payment_type == 'transfer':
				continue
			domain = self._get_moves_domain()
			pending_invoices = move_model.search(domain, order="invoice_date_due ASC")
			pending_amount = rec.amount
			rec.payment_line_ids.filtered(lambda line: not line.is_main or line.display_type == 'asset_cash').unlink()
			for invoice in pending_invoices:
				for aml in self._filter_amls(invoice.line_ids):
					amount_to_apply = 0
					amount_residual = rec.company_id.currency_id._convert(
						aml.amount_residual,
						rec.currency_id,
						rec.company_id,
						date=rec.date,
					)
					if pending_amount >= 0:
						amount_to_apply = min(abs(amount_residual), pending_amount)
						pending_amount -= abs(amount_residual)
						# Check if both amounts are negative to adjust the sign

					rec._hook_create_new_line(invoice, aml, amount_to_apply,amount_residual)
			rec._recompute_dynamic_lines_payment()

	def action_delete_counterpart_lines(self):
		if self.payment_line_ids and self.state == "draft":
			self.payment_line_ids = [(5, 0, 0)]
			self._recompute_dynamic_lines_payment()

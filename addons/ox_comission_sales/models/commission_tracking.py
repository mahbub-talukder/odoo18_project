from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class CommissionTracking(models.Model):
    _name = 'commission.tracking'
    _description = 'Commission Tracking'
    _rec_name = 'sale_order_id'
    
    sale_order_id = fields.Many2one('sale.order', string='Sales Order', required=True)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', required=True)
    commission_plan_id = fields.Many2one('commission.plan', string='Commission Plan', required=True)
    disbursement_frequency = fields.Selection(related='commission_plan_id.disbursement_frequency', 
                                              string='Disbursement Frequency', store=True)
    customer_id = fields.Many2one('res.partner', string='Customer', 
                                   related='sale_order_id.partner_id', store=True)
    
    order_amount = fields.Monetary(string='Order Amount', currency_field='currency_id')
    commission_type = fields.Selection([
        ('first_order', 'First Order'),
        ('residual', 'Residual')
    ], string='Commission Type', required=True)
    
    commission_percentage = fields.Float(string='Commission %',aggregator=False)
    commission_amount = fields.Monetary(string='Commission Amount', 
                                        currency_field='currency_id', compute='_compute_commission_amount', store=True)
    
    invoice_id = fields.Many2one('account.move', string='Customer Invoice')
    invoice_payment_state = fields.Selection(
        related='invoice_id.payment_state',
        string='Invoice Payment Status',
        store=True,
    )
   
    vendor_bill_id = fields.Many2one('account.move', string='Vendor Bill')
    vendor_bill_state = fields.Selection(related='vendor_bill_id.state', 
                                         string='Vendor Bill Status')
    
    disbursement_date = fields.Date(string='Disbursement Date')
    is_paid = fields.Boolean(string='Is Paid', default=False)
    
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                   default=lambda self: self.env.company.currency_id)
    
    # ------------------------------------------------------------------
    # Smart button helpers
    # ------------------------------------------------------------------
    def _open_record_action(self, model, res_id):
        """Return a simple ir.actions.act_window opening a specific record.

        Using a minimal action avoids depending on external action XML ids and
        works across installations.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'View',
            'res_model': model,
            'view_mode': 'form',
            'target': 'current',
            'res_id': res_id,
        }

    def action_open_vendor_bill(self):
        self.ensure_one()
        if not self.vendor_bill_id:
            return False
        return self._open_record_action('account.move', self.vendor_bill_id.id)

    def action_open_customer_invoice(self):
        self.ensure_one()
        if not self.invoice_id:
            return False
        return self._open_record_action('account.move', self.invoice_id.id)

    def action_open_sale_order(self):
        self.ensure_one()
        if not self.sale_order_id:
            return False
        return self._open_record_action('sale.order', self.sale_order_id.id)

    # @api.model
    # def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
    #     """Augment grouped results with a consolidated invoice payment status.

    #     We do NOT override the native aggregated value of invoice_payment_state
    #     (which is a count). Instead, we populate a separate summary field that
    #     the list view can display only for grouped rows.
    #     """
    #     res = super().read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)

    #     needs_summary = (
    #         'invoice_payment_state_summary' in fields
    #         or any(f.startswith('invoice_payment_state_summary') for f in fields)
    #         or 'invoice_payment_state' in fields
    #         or any(f.startswith('invoice_payment_state:') for f in fields)
    #     )

    #     if needs_summary:
    #         for line in res:
    #             group_domain = line.get('__domain')
    #             if not group_domain:
    #                 continue
    #             records = self.search(group_domain)
    #             states = set(records.mapped('invoice_payment_state'))

    #             # Determine consolidated state: paid if all paid; partial if any partial; else not_paid
    #             if states == {'paid'}:
    #                 summary = 'paid'
    #             elif 'partial' in states and 'paid' in states and len(states) == 2:
    #                 summary = 'partial'
    #             elif 'partial' in states:
    #                 summary = 'partial'
    #             else:
    #                 summary = 'not_paid'

    #             line['invoice_payment_state_summary'] = summary

    #     return res
    
    def _compute_invoice_payment_state_summary(self):
        for record in self:
            record.invoice_payment_state_summary = 0

    @api.depends('order_amount', 'commission_percentage')
    def _compute_commission_amount(self):
        for record in self:
            record.commission_amount = (record.order_amount * record.commission_percentage) / 100
                     
    # Add method to check if customer is first-time buyer
    def _is_first_order(self, customer_id, salesperson_id):
        previous_orders = self.env['sale.order'].search_count([
            ('partner_id', '=', customer_id),
            ('user_id', '=', salesperson_id),
            ('state', 'in', ['sale', 'done']),
            ('id', '!=', self.sale_order_id.id)
        ])
        return previous_orders == 0
    

    @api.model
    def cron_generate_vendor_bills(self):
        """Cron job to generate vendor bills based on disbursement frequency"""
        today = fields.Date.today()

        # find the active commission plans
        active_commission_plan = self.env['commission.plan'].search([
            ('state', '=', 'approved'),
            ('target_period_start', '<=', today),
            ('target_period_end', '>=', today)
        ], limit=1)
        
        if active_commission_plan.cron_run_date :
            today = active_commission_plan.cron_run_date

        _logger.info(f"Today: {today},weekday: {today.weekday()},day: {today.day}")
        # return True
        # Get all unpaid commissions with paid invoices
        unpaid_commissions = self.search([
            ('is_paid', '=', False),
            ('invoice_payment_state', '=', 'paid'),
            ('vendor_bill_id', '=', False)
        ])
        
        # Group by salesperson and disbursement frequency
        commission_groups = {}
        for commission in unpaid_commissions:
            key = (commission.salesperson_id.id, 
                commission.commission_plan_id.disbursement_frequency)
            if key not in commission_groups:
                commission_groups[key] = []
            commission_groups[key].append(commission)
        
        # Create vendor bills
        for (salesperson_id, frequency), commissions in commission_groups.items():
            if self._should_generate_bill(frequency, today):
                self._create_vendor_bill(salesperson_id, commissions)
                
    def _should_generate_bill(self, frequency, date):
        """Check if bill should be generated based on frequency"""
        if frequency == 'weekly':
            return date.weekday() == 0  # Monday
        elif frequency == 'biweekly':
            # Generate on 1st and 15th of month
            return date.day in [1, 15]
        elif frequency == 'monthly':
            return date.day == 1
        return False
        
    def _create_vendor_bill(self, salesperson_id, commissions):
        """Create vendor bill for commission payment"""
        salesperson = self.env['res.users'].browse(salesperson_id)
        
        # Create vendor bill
        bill_vals = {
            'move_type': 'in_invoice',
            'partner_id': salesperson.partner_id.id,
            'invoice_date': fields.Date.today(),
            'ref': f"Commission Payment - {salesperson.name}",
            'invoice_line_ids': []
        }
        
        for commission in commissions:
            line_vals = (0, 0, {
                'name': f"Commission for SO {commission.sale_order_id.name}",
                'quantity': 1,
                'price_unit': commission.commission_amount,
                'account_id': self._get_commission_expense_account().id,
            })
            bill_vals['invoice_line_ids'].append(line_vals)
        
        vendor_bill = self.env['account.move'].create(bill_vals)
        
        # Link vendor bill to commissions
        for commission in commissions:
            commission.vendor_bill_id = vendor_bill.id
            commission.disbursement_date = fields.Date.today()
        
        return vendor_bill
        
    def _get_commission_expense_account(self):
        """Get or create commission expense account"""
        # In Odoo 18, account.account uses company_ids (Many2many) instead of company_id
        # Using standard commission expense account code 6220
        account = self.env['account.account'].search([
            ('code', '=', '6220'),
            ('company_ids', 'in', [self.env.company.id])
        ], limit=1)
        
        if not account:
            account = self.env['account.account'].create({
                'code': '6220',
                'name': 'Commission Expense',
                'account_type': 'expense_direct_cost',
                'company_ids': [(6, 0, [self.env.company.id])],
            })
        return account
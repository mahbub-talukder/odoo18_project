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
    
    commission_percentage = fields.Float(string='Commission %')
    commission_amount = fields.Monetary(string='Commission Amount', 
                                        currency_field='currency_id', compute='_compute_commission_amount', store=True)
    
    invoice_id = fields.Many2one('account.move', string='Customer Invoice')
    invoice_payment_state = fields.Selection(related='invoice_id.payment_state', 
                                             string='Invoice Payment Status', store=True)
    
    vendor_bill_id = fields.Many2one('account.move', string='Vendor Bill')
    vendor_bill_state = fields.Selection(related='vendor_bill_id.state', 
                                         string='Vendor Bill Status')
    
    disbursement_date = fields.Date(string='Disbursement Date')
    is_paid = fields.Boolean(string='Is Paid', default=False)
    
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                   default=lambda self: self.env.company.currency_id)
    
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
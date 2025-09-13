from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SalesCommissionRealtimeReportDetail(models.Model):
    _name = 'sales.commission.realtime.report.detail'
    _description = 'Real-time Commission Report Detail'
    _auto = False  # This is a SQL view, not a stored table

    # source information
    source_type = fields.Selection([
        ('sale_order', 'Sale Order'),
        ('invoice', 'Invoice')
    ], string="Source Type", readonly=True)

    document_number = fields.Char(string="Document Number", readonly=True)

    # source id
    sales_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)
    invoice_id = fields.Many2one('account.move', string="Invoice", readonly=True)

    # document information
    partner_id = fields.Many2one('res.partner', string="Partner", readonly=True)
    salesperson_id = fields.Many2one('res.users', string="Salesperson", readonly=True)
 
    date_achievement = fields.Date(string="Achievement Date", readonly=True)
    # Achievement amounts
    achieved_amount = fields.Monetary(string="Achieved Amount", readonly=True)
    achieved_units = fields.Float(string="Achieved Units", readonly=True)

    # product information
    product_id = fields.Many2one('product.product', string="Product", readonly=True)
    product_category_id = fields.Many2one('product.category', string="Product Category", readonly=True)
     
    # Additional fields
    currency_id = fields.Many2one('res.currency', string="Currency", readonly=True)

    def action_view_document(self):
        """Open related document"""
        self.ensure_one()
        if self.source_type == 'sale_order':
            return self.sales_order_id.action_view_sale_order()
        elif self.source_type == 'invoice':
            return self.invoice_id.action_view_invoice()
   
    @property
    def _table_query(self):
        return """
        WITH 
        sale_order_data AS (
            SELECT
                'sale_order' as source_type,
                so.name as document_number,
                so.id as sales_order_id,
                NULL::integer as invoice_id,
                so.partner_id as partner_id,
                so.user_id as salesperson_id,
                so.date_order as date_achievement,
                so.currency_id as currency_id,
                sol.price_total as achieved_amount,
                sol.product_uom_qty as achieved_units,
                pp.id as product_id,
                pc.id as product_category_id,
                sol.id as line_id
            FROM sale_order so
            JOIN sale_order_line sol ON sol.order_id = so.id 
                AND sol.display_type IS NULL
            JOIN product_product pp ON pp.id = sol.product_id
            JOIN product_template pt ON pt.id = pp.product_tmpl_id
            JOIN product_category pc ON pc.id = pt.categ_id
            WHERE so.state IN ('sale', 'done')
        ),
        invoice_data AS (
            SELECT
                'invoice' as source_type,
                am.name as document_number,
                NULL::integer as sales_order_id,
                am.id as invoice_id,
                am.partner_id as partner_id,
                am.invoice_user_id as salesperson_id,
                am.invoice_date as date_achievement,
                am.currency_id as currency_id,
                aml.price_total as achieved_amount,
                aml.quantity as achieved_units,
                pp.id as product_id,
                pc.id as product_category_id,
                aml.id as line_id
            FROM account_move am
            JOIN account_move_line aml ON aml.move_id = am.id
                AND aml.display_type IS NOT NULL
                AND aml.product_id IS NOT NULL
            JOIN product_product pp ON pp.id = aml.product_id
            JOIN product_template pt ON pt.id = pp.product_tmpl_id
            JOIN product_category pc ON pc.id = pt.categ_id
            WHERE am.move_type = 'out_invoice'
                    AND am.state = 'posted'
                    AND am.invoice_user_id is not null and am.invoice_user_id != 0
        ),
        combined_data AS (
            SELECT * FROM sale_order_data
            UNION ALL
            SELECT * FROM invoice_data
        )
        SELECT 
            ROW_NUMBER() OVER (ORDER BY date_achievement DESC, document_number, source_type, line_id) as id,
            source_type,
            document_number,
            sales_order_id,
            invoice_id,
            partner_id,
            salesperson_id,
            date_achievement,
            currency_id,
            achieved_amount,
            achieved_units,
            product_id,
            product_category_id
        FROM combined_data
        """
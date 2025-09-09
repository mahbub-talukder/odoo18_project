from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SalesCommissionRealtimeReport(models.Model):
    _name = 'sales.commission.realtime.report'
    _description = 'Real-time Commission Report (SQL View)'
    _auto = False  # This is a SQL view, not a stored table
    _order = 'period desc, salesperson_id'

    # Main identifiers
    salesperson_id = fields.Many2one('res.users', string="Salesperson", readonly=True)
    team_id = fields.Many2one('crm.team', string="Sales Team", readonly=True)
    plan_id = fields.Many2one('sales.commission', string="Commission Plan", readonly=True)
    target_id = fields.Many2one('sales.commission.target', string="Target Period", readonly=True)
    period = fields.Char(string="Period", readonly=True)
    
    # Plan details
    commission_type = fields.Selection([
        ('qty', 'Based on Quantity'),
        ('volume', 'Based on Volume')
    ], string="Commission Type", readonly=True)
    qualification_criteria = fields.Selection([
        ('so_amount', 'Sale Order Amount'),
        ('amount_invoiced', 'Amount Invoiced'),
        ('qty_sold', 'Quantity Sold'),
        ('qty_invoiced', 'Quantity Invoiced')
    ], string="Qualification Criteria", readonly=True)
    
    # Target fields
    target_amount = fields.Monetary(string="Target Amount", readonly=True, currency_field='currency_id')
    target_units = fields.Float(string="Target Units", readonly=True)
    collection_target = fields.Monetary(string="Collection Target", readonly=True, currency_field='currency_id')
    
    # Achievement fields  
    achieved_amount = fields.Monetary(string="Achieved Amount", readonly=True, currency_field='currency_id')
    achieved_units = fields.Float(string="Achieved Units", readonly=True)
    collection_amount = fields.Monetary(string="Collection Amount", readonly=True, currency_field='currency_id')
    achievement_rate = fields.Float(string="Achievement Rate (%)", readonly=True)
    
    # Commission fields
    commission_earned = fields.Monetary(string="Commission Earned", readonly=True, currency_field='currency_id')
    paid_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('partially_paid', 'Partially Paid'),
        ('paid', 'Paid'),
        ('overpaid', 'Overpaid')
    ], string="Paid Status",  readonly=True)


    
    commission_slab_id = fields.Many2one('sales.commission.line', string="Applied Commission Slab", readonly=True)
    
    # System fields
    company_id = fields.Many2one('res.company', string="Company", readonly=True)
    currency_id = fields.Many2one('res.currency', string="Currency", readonly=True)
    
    # Period status
    period_status = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('active', 'Active'), 
        ('completed', 'Completed'),
        ('closed', 'Closed')
    ], string="Period Status", readonly=True)
    
    # Date fields for filtering
    date_from = fields.Date(string="Period Start", readonly=True)
    date_to = fields.Date(string="Period End", readonly=True)
    # bill generated
    bill_id = fields.Many2one('account.move', string="Vendor Bill", readonly=True)
    bill_generated = fields.Boolean(string="Bill Generated", readonly=True)
    
    @property
    def _table_query(self):
        """
        Generate the SQL query that creates this view.
        This replaces the stored commission report with real-time calculation.
        """
        return f"""
            WITH plan_users AS (
                -- Get all user-plan combinations (individual plans)
                SELECT 
                    sp.id as plan_id,
                    u.id as user_id,
                    sp.commission_type,
                    sp.qualification_criteria,
                    sp.commission_for,
                    sp.team_id,
                    sp.company_id,
                    sp.currency_id,
                    sp.state as plan_state
                FROM sales_commission sp
                JOIN res_users_sales_commission_rel rel ON rel.sales_commission_id = sp.id
                JOIN res_users u ON u.id = rel.res_users_id
                WHERE  sp.commission_for = 'person' AND sp.state in ('approved', 'done')
                
                UNION
                
                -- Team-based plans
                SELECT 
                    sp.id as plan_id,
                    tm.user_id as user_id,
                    sp.commission_type,
                    sp.qualification_criteria,
                    sp.commission_for,
                    sp.team_id,
                    sp.company_id,
                    sp.currency_id,
                    sp.state as plan_state
                FROM sales_commission sp
                JOIN crm_team_member tm ON tm.crm_team_id = sp.team_id
                WHERE sp.commission_for = 'team' AND sp.state in ('approved', 'done')
            ),
            
            sale_achievements AS (
                -- Calculate achievements from sale orders
                SELECT 
                    pu.plan_id,
                    pu.user_id,
                    st.id as target_id,
                    st.period,
                    st.date_from,
                    st.date_to,
                    SUM(CASE 
                        WHEN pu.commission_type = 'volume' THEN sol.price_total
                        ELSE 0 
                    END) as achieved_amount,
                    SUM(CASE 
                        WHEN pu.commission_type = 'qty' THEN sol.product_uom_qty
                        ELSE 0 
                    END) as achieved_units,
                    0 as collection_amount
                FROM plan_users pu
                JOIN sales_commission sp ON sp.id = pu.plan_id
                JOIN sales_commission_target st ON st.plan_id = pu.plan_id
                JOIN sale_order so ON so.user_id = pu.user_id 
                    AND so.date_order >= st.date_from 
                    AND so.date_order <= st.date_to
                    AND so.state IN ('sale', 'done')
                JOIN sale_order_line sol ON sol.order_id = so.id 
                    AND sol.display_type IS NULL
                WHERE pu.qualification_criteria IN ('so_amount', 'qty_sold') 
                AND st.period_status != 'upcoming'
                AND (
                    -- Filter by products if defined in the commission plan
                    NOT EXISTS (
                        SELECT 1 FROM sales_commission_product_rel pr 
                        WHERE pr.commission_id = sp.id
                    )
                    OR 
                    EXISTS (
                        SELECT 1 FROM sales_commission_product_rel pr 
                        WHERE pr.commission_id = sp.id AND pr.product_id = sol.product_id
                    )
                )
                AND (
                    -- Filter by product categories if defined in the commission plan
                    NOT EXISTS (
                        SELECT 1 FROM sales_commission_category_rel cr 
                        WHERE cr.commission_id = sp.id
                    )
                    OR 
                    EXISTS (
                        SELECT 1 FROM sales_commission_category_rel cr 
                        JOIN product_product pp ON pp.id = sol.product_id
                        JOIN product_template pt ON pt.id = pp.product_tmpl_id
                        WHERE cr.commission_id = sp.id AND cr.category_id = pt.categ_id
                    )
                )
                GROUP BY pu.plan_id, pu.user_id, st.id, st.period, st.date_from, st.date_to
            ),
            
            invoice_achievements AS (
                -- Calculate achievements from invoices
                SELECT 
                    pu.plan_id,
                    pu.user_id,
                    st.id as target_id,
                    st.period,
                    st.date_from,
                    st.date_to,
                    SUM(CASE 
                        WHEN pu.commission_type = 'volume' THEN aml.price_total
                        ELSE 0 
                    END) as achieved_amount,
                    SUM(CASE 
                        WHEN pu.commission_type = 'qty' THEN aml.quantity
                        ELSE 0 
                    END) as achieved_units,
                    -- Calculate the total paid amount for the invoices
                    SUM(CASE 
                        WHEN pu.qualification_criteria = 'amount_invoiced' AND am.payment_state IN ('paid', 'in_payment') 
                        THEN aml.price_total
                        ELSE 0 
                    END) as collection_amount
                FROM plan_users pu
                JOIN sales_commission sp ON sp.id = pu.plan_id
                JOIN sales_commission_target st ON st.plan_id = pu.plan_id
                JOIN account_move am ON am.invoice_user_id = pu.user_id 
                    AND am.invoice_date >= st.date_from 
                    AND am.invoice_date <= st.date_to
                    AND am.move_type = 'out_invoice'
                    AND am.state = 'posted'
                JOIN account_move_line aml ON aml.move_id = am.id 
                    AND aml.display_type IS NOT NULL
                    AND aml.product_id IS NOT NULL
                JOIN sale_order_line_invoice_rel slir ON slir.invoice_line_id = aml.id
                JOIN sale_order_line sol ON sol.id = slir.order_line_id
                JOIN sale_order so ON so.id = sol.order_id AND so.user_id = pu.user_id
                WHERE pu.qualification_criteria IN ('amount_invoiced', 'qty_invoiced')
                AND st.period_status != 'upcoming'
                AND (
                    -- Filter by products if defined in the commission plan
                    NOT EXISTS (
                        SELECT 1 FROM sales_commission_product_rel pr 
                        WHERE pr.commission_id = sp.id
                    )
                    OR 
                    EXISTS (
                        SELECT 1 FROM sales_commission_product_rel pr 
                        WHERE pr.commission_id = sp.id AND pr.product_id = aml.product_id
                    )
                )
                AND (
                    -- Filter by product categories if defined in the commission plan
                    NOT EXISTS (
                        SELECT 1 FROM sales_commission_category_rel cr 
                        WHERE cr.commission_id = sp.id
                    )
                    OR 
                    EXISTS (
                        SELECT 1 FROM sales_commission_category_rel cr 
                        JOIN product_product pp ON pp.id = aml.product_id
                        JOIN product_template pt ON pt.id = pp.product_tmpl_id
                        WHERE cr.commission_id = sp.id AND cr.category_id = pt.categ_id
                    )
                )
                GROUP BY pu.plan_id, pu.user_id, st.id, st.period, st.date_from, st.date_to
            ),
            
            combined_achievements AS (
                -- Combine sale and invoice achievements
                SELECT * FROM sale_achievements
                UNION ALL
                SELECT * FROM invoice_achievements
            ),
            
            total_achievements AS (
                -- Sum up achievements by plan, user, target
                SELECT 
                    plan_id,
                    user_id,
                    target_id,
                    period,
                    date_from,
                    date_to,
                    SUM(achieved_amount) as total_achieved_amount,
                    SUM(achieved_units) as total_achieved_units,
                    SUM(collection_amount) as total_collection_amount
                FROM combined_achievements
                GROUP BY plan_id, user_id, target_id, period, date_from, date_to
            ),
            
            commission_calculation AS (
                -- Calculate commission based on achievements and slabs
                SELECT 
                    -- plan details (selected plan users)
                    pu.plan_id,
                    pu.user_id,

                    -- plan details (selected plan)
                    sp.commission_type,
                    sp.qualification_criteria,
                    sp.team_id,
                    sp.company_id,
                    sp.currency_id,

                    -- target details
                    st.id as target_id,
                    st.period,
                    st.date_from,
                    st.date_to,
                    st.target_amount,
                    st.target_units,
                    st.collection_target,
                    st.period_status,

                    -- achievement details
					CASE 
						when ta.total_achieved_amount is not null then ta.total_achieved_amount
						else 0
					END as total_achieved_amount,

					CASE 
						when ta.total_achieved_units is not null then ta.total_achieved_units
						else 0
					END as total_achieved_units,

                    CASE 
                        when ta.total_collection_amount is not null then ta.total_collection_amount
                        else 0
                    END as total_collection_amount,

                    -- Calculate achievement rate
                    CASE 
                        WHEN sp.commission_type = 'volume' AND st.target_amount > 0 
                        THEN ta.total_achieved_amount / st.target_amount * 100
                        WHEN sp.commission_type = 'qty' AND st.target_units > 0 
                        THEN ta.total_achieved_units / st.target_units * 100
                        ELSE 0
                    END as achievement_rate,
                    -- Find applicable commission slab (highest applicable)
                    (SELECT scl.commission_amount 
                     FROM sales_commission_line scl 
                     WHERE scl.target_id = ta.target_id 
                       AND scl.completion_percent <= CASE 
                           WHEN sp.qualification_criteria = 'amount_invoiced' AND st.target_amount > 0 
                           and st.collection_target > ta.total_collection_amount
                           THEN 0
                           WHEN sp.commission_type = 'volume' AND st.target_amount > 0 
                           THEN ta.total_achieved_amount / st.target_amount
                           WHEN sp.commission_type = 'qty' AND st.target_units > 0 
                           THEN ta.total_achieved_units / st.target_units
                           ELSE 0
                          END
                     ORDER BY scl.completion_percent DESC 
                     LIMIT 1) as commission_earned,
                    -- Get the slab ID
                    (SELECT scl.id 
                     FROM sales_commission_line scl 
                     WHERE scl.target_id = ta.target_id 
                       AND scl.completion_percent <= CASE 
                           WHEN sp.qualification_criteria = 'amount_invoiced' AND st.target_amount > 0 
                                and st.collection_target > ta.total_collection_amount
                           THEN 0
                           WHEN sp.commission_type = 'volume' AND st.target_amount > 0 
                           THEN ta.total_achieved_amount / st.target_amount
                           WHEN sp.commission_type = 'qty' AND st.target_units > 0 
                           THEN ta.total_achieved_units / st.target_units
                           ELSE 0
                       END
                     ORDER BY scl.completion_percent DESC 
                     LIMIT 1) as commission_slab_id
                     
                -- FROM total_achievements ta
                -- JOIN sales_commission sp ON sp.id = ta.plan_id
                -- JOIN sales_commission_target st ON st.id = ta.target_id

                FROM sales_commission_target st
                JOIN sales_commission sp  ON sp.id = st.plan_id
				JOIN plan_users pu on pu.plan_id = sp.id
                LEFT JOIN total_achievements ta ON sp.id = ta.plan_id and st.id = ta.target_id and pu.user_id = ta.user_id
                WHERE st.period_status != 'upcoming'
            )
            
            -- Final SELECT with row numbering for unique IDs
            SELECT 
                ROW_NUMBER() OVER (ORDER BY cc.period DESC, cc.user_id, cc.plan_id) as id,
                cc.user_id as salesperson_id,
                cc.team_id,
                cc.plan_id,
                cc.target_id,
                cc.period,
                cc.commission_type,
                cc.qualification_criteria,
                cc.target_amount,
                cc.target_units,
                cc.collection_target,
                cc.total_achieved_amount as achieved_amount,
                cc.total_achieved_units as achieved_units,
                cc.total_collection_amount as collection_amount,
                cc.achievement_rate,
                COALESCE(cc.commission_earned, 0) as commission_earned,
                cc.commission_slab_id,
                cc.company_id,
                cc.currency_id,
                cc.period_status,
                cc.date_from,
                cc.date_to,
                sr.bill_generated,
                CASE 
                    WHEN sr.bill_id IS NULL THEN 'unpaid'
                    WHEN am.payment_state = 'paid' THEN 'paid'
                    WHEN am.payment_state = 'partial' THEN 'partially_paid'
                    WHEN am.payment_state = 'in_payment' THEN 'partially_paid'
                    ELSE 'unpaid'
                END as paid_status,
                sr.bill_id
            
            FROM commission_calculation cc
            LEFT JOIN sales_commission_report sr 
                ON sr.salesperson_id = cc.user_id 
                and sr.plan_id = cc.plan_id 
                and sr.target_id = cc.target_id
            LEFT JOIN account_move am ON am.id = sr.bill_id
            -- comment this out to show all plans and targets
            -- WHERE (cc.total_achieved_amount > 0 OR cc.total_achieved_units > 0) OR cc.period_status IN ('active', 'upcoming') 
           
        """

    
    def action_view_details(self):
        """View detailed breakdown of this commission"""
        self.ensure_one()
        
        # Use the new detailed SQL view to show commission breakdown
        domain = [
            ('salesperson_id', '=', self.salesperson_id.id),
            ('date_achievement', '>=', self.date_from),
            ('date_achievement', '<=', self.date_to),
        ]
        
        # Filter by source type based on qualification criteria
        if self.qualification_criteria in ['so_amount', 'qty_sold']:
            domain.append(('source_type', '=', 'sale_order'))
        elif self.qualification_criteria in ['amount_invoiced', 'qty_invoiced']:
            domain.append(('source_type', '=', 'invoice'))

        if self.plan_id.product_ids:
            domain.append(('product_id', 'in', self.plan_id.product_ids.ids))
        elif self.plan_id.category_ids:
            domain.append(('product_category_id', 'in', self.plan_id.category_ids.ids))
        
        return {
            'type': 'ir.actions.act_window',
            'name': f'Commission Details - {self.period} ({self.salesperson_id.name})',
            'res_model': 'sales.commission.realtime.report.detail',
            'view_mode': 'list,form',
            'domain': domain,
            'context': {
                'create': False,
                'search_default_group_by_document_number': 1
            },
            'target': 'current',
        }
    
    def action_view_vendor_bill(self):
        """Open related vendor bill"""
        self.ensure_one()
        if not self.bill_id:
            return False
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vendor Bill',
            'res_model': 'account.move',
            'res_id': self.bill_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
    @api.model
    def get_commission_summary(self, user_id=None):
        """Get commission summary for dashboard/reports"""
        domain = []
        if user_id:
            domain.append(('salesperson_id', '=', user_id))
        
        commissions = self.search(domain)
        
        return {
            'total_earned': sum(commissions.mapped('commission_earned')),
            'active_plans': len(commissions.mapped('plan_id')),
            'current_period_earnings': sum(
                commissions.filtered(lambda c: c.period_status == 'active').mapped('commission_earned')
            ),
        } 
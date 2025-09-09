from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class SalesCommissionLine(models.Model):
    _name = 'sales.commission.line'
    _description = 'Commission Slab'
 
    target_id = fields.Many2one('sales.commission.target', ondelete='cascade', string="Commission Target")
    
    completion_target_units = fields.Float(string="Target Units")
    completion_target_amount = fields.Monetary(string="Target Amount", currency_field='currency_id')
    completion_percent = fields.Float(string="Target Completion (%)")
    commission_amount = fields.Monetary(string="Commission Amount", currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', related='target_id.currency_id', store=True, readonly=True)
    
    # Related fields needed for conditional visibility in dialog views
    commission_type = fields.Char(string="Commission Type",  compute='_compute_commission_details', store=True)
       
    qualification_criteria = fields.Char(string="Qualification Criteria", compute='_compute_qualification_criteria', store=True)



    @api.depends('target_id.plan_id.commission_type')
    def _compute_commission_details(self): 
        for record in self:
            _logger.info(f"""Computing commission type for slab {record.id}, target id: {record.target_id.id}, target plan id: {record.target_id.plan_id.id}""")
            if record.target_id and record.target_id.plan_id:
                record.commission_type = record.target_id.plan_id.commission_type
                
            else:
                record.commission_type = ''

    @api.depends('target_id.plan_id.qualification_criteria')
    def _compute_qualification_criteria(self):
        for record in self:
            _logger.info(f"""Computing qualification criteria for slab {record.id}, target id: {record.target_id.id}, 
                         target plan id: {record.target_id.plan_id.id}""")
            if record.target_id and record.target_id.plan_id:
                record.qualification_criteria = record.target_id.plan_id.qualification_criteria
            else:
                record.qualification_criteria = ''

    
    @api.constrains('completion_target_units', 'completion_target_amount', 'completion_percent')
    def _check_reasonable_targets(self):
        """Validate that completion targets are reasonable compared to base targets"""
        for record in self:
            if not record.target_id:
                continue
                
            # For quantity-based plans
            if record.target_id.plan_id.commission_type == 'qty':
                
                if not record.target_id.target_units or record.target_id.target_units <= 0:
                    raise ValidationError(
                        f"Please set a valid Target Units for period '{record.target_id.period}' before adding commission slabs."
                    )
                    
                
            
            # For volume-based plans            
            elif record.target_id.plan_id.commission_type == 'volume':
                
                if not record.target_id.target_amount or record.target_id.target_amount <= 0:
                    raise ValidationError(
                        f"Please set a valid Target Amount for period '{record.target_id.period}' before adding commission slabs."
                    )
                    
            
            # Check percentage is reasonable percentage between 0 to 1000% (as decimal: 0 to 10)
            if record.completion_percent and (record.completion_percent > 10 or record.completion_percent < 0):
                # Convert to percentage for display
                percent_display = record.completion_percent * 100
                raise ValidationError(
                    f"Target Completion Percentage ({percent_display:.1f}%) should be between 0% and 1000%. "
                    f"Please enter a reasonable percentage."
                )

    @api.onchange('completion_target_units')
    def _onchange_completion_target_units(self):
        """Calculate completion_percent when completion_target_units is changed (for qty-based plans)"""
        if self.target_id and  self.target_id.plan_id.commission_type == 'qty':
            self.completion_target_amount = 0.0
            if not self.target_id.target_units or self.target_id.target_units <= 0:
                self.completion_percent = 0.0
                
                return {
                    'warning': {
                        'title': 'Missing Target Units',
                        'message': f'Please set Target Units for period "{self.target_id.period}" first.\n'
                                f'Go to the Target tab and set the Target Units before configuring commission slabs.'
                    }
                }

            # Calculate percentage - Odoo percentage widget stores as decimal (0.75 for 75%)
            new_percent = self.completion_target_units / self.target_id.target_units
            _logger.info(f"Units calculation: {self.completion_target_units} / {self.target_id.target_units} = {new_percent:.4f} (as decimal)")
            _logger.info(f"Current Completion Percent: {self.completion_percent}, new_percent: {new_percent}")
            self.completion_percent = new_percent 
        
       
        

    @api.onchange('completion_target_amount')
    def _onchange_completion_target_amount(self):
        """Calculate completion_percent when completion_target_amount is changed (for volume-based plans)"""
        _logger.info(f"Commission Type: {self.commission_type},from main model-->{self.target_id.plan_id.commission_type}")
        _logger.info(f"Completion Target Amount: {self.completion_target_amount}")
        if self.target_id and self.target_id.plan_id.commission_type == 'volume':
            self.completion_target_units = 0.0
            
    
            if not self.target_id.target_amount or self.target_id.target_amount <= 0:
                self.completion_percent = 0.0
                return {
                    'warning': {
                        'title': 'Missing Target Amount',
                        'message': f'Please set Target Amount for period "{self.target_id.period}" first.\n'
                                f'Go to the Target tab and set the Target Amount before configuring commission slabs.'
                    }
                }

            # Calculate percentage - Odoo percentage widget stores as decimal (0.75 for 75%)
            new_percent = self.completion_target_amount / self.target_id.target_amount
            _logger.info(f"Amount calculation: {self.completion_target_amount} / {self.target_id.target_amount} = {new_percent:.4f} (as decimal)")
            _logger.info(f"Current Completion Percent: {self.completion_percent}, new_percent: {new_percent}")
            self.completion_percent = new_percent 
        

    @api.onchange('completion_percent')
    def _onchange_completion_percent(self):
        """Calculate completion_target_units/completion_target_amount when completion_percent is changed"""
        _logger.info(f"Commission Type: {self.commission_type},from main model-->{self.target_id.plan_id.commission_type}")
        _logger.info(f"Completion Percent (as decimal): {self.completion_percent}")
        if not self.completion_percent:
            if self.target_id:
                if self.target_id.plan_id.commission_type == 'qty':
                    self.completion_target_units = 0.0
                elif self.target_id.plan_id.commission_type == 'volume':
                    self.completion_target_amount = 0.0
            return

    
        # For quantity-based commissions
        if self.target_id.plan_id.commission_type == 'qty':
            if not self.target_id.target_units or self.target_id.target_units <= 0:
                return {
                    'warning': {
                        'title': 'Missing Target Units',
                        'message': f'Please set Target Units for period "{self.target_id.period}" first.\n'
                                  f'Go to the Target tab and set the Target Units before configuring commission slabs.'
                    }
                }
                
            # completion_percent is stored as decimal (0.75 for 75%)
            new_units = self.completion_percent * self.target_id.target_units
            _logger.info(f"Percent to Units: {self.completion_percent} * {self.target_id.target_units} = {new_units}")
            self.completion_target_units = new_units
            
        # For volume-based commissions
        elif self.target_id.plan_id.commission_type == 'volume':
            if not self.target_id.target_amount or self.target_id.target_amount <= 0:
                return {
                    'warning': {
                        'title': 'Missing Target Amount',
                        'message': f'Please set Target Amount for period "{self.target_id.period}" first.\n'
                                  f'Go to the Target tab and set the Target Amount before configuring commission slabs.'
                    }
                }
                
            # completion_percent is stored as decimal (0.75 for 75%)
            new_amount = self.completion_percent * self.target_id.target_amount
            _logger.info(f"Percent to Amount: {self.completion_percent} * {self.target_id.target_amount} = {new_amount}")
            self.completion_target_amount = new_amount
            
    def action_delete_slab(self):
        """Custom delete method that keeps dialog open"""
        self.ensure_one()
        target_id = self.target_id.id
        self.unlink()
        
        # Return action to reopen the dialog with updated data
        return {
            'type': 'ir.actions.act_window',
            'name': 'Commission Slabs',
            'res_model': 'sales.commission.line',
            'view_mode': 'list',
            'view_id': self.env.ref('ox_sales_commission.sales_commission_line_tree_view').id,
            'target': 'new',
            'domain': [('target_id', '=', target_id)],
            'context': {
                'default_target_id': target_id,
                'commission_type': self.env['sales.commission.target'].browse(target_id).plan_id.commission_type,
                'qualification_criteria': self.env['sales.commission.target'].browse(target_id).plan_id.qualification_criteria,
            }
        }    
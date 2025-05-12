from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class UnifiedSalesExternalOrder(models.Model):
    _name = 'unified.sales.external.order'
    _description = 'External Sales Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_created desc'

    name = fields.Char(string='Order Reference', required=True, copy=False, 
                      readonly=True, default=lambda self: _('New'))
    external_id = fields.Char(string='External ID', required=True, copy=False)
    api_config_id = fields.Many2one('unified.sales.api.config', string='API Configuration', 
                                   required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    quotation_id = fields.Many2one('sale.order', string='Quotation', tracking=True)
    date_created = fields.Datetime(string='Created Date', required=True, default=fields.Datetime.now)
    last_update = fields.Datetime(string='Last Update', default=fields.Datetime.now)
    state = fields.Selection([
        ('new', 'New'),
        ('processed', 'Processed'),
        ('error', 'Error')
    ], string='Status', default='new', tracking=True)
    error_message = fields.Text(string='Error Message')
    external_data = fields.Text(string='External Data')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('unified.sales.external.order') or _('New')
        return super().create(vals_list)

    def action_process(self):
        """Process the external order and create a quotation."""
        self.ensure_one()
        if self.state != 'new':
            raise UserError(_('Only new orders can be processed.'))

        try:
            # Create quotation
            quotation_vals = {
                'partner_id': self.partner_id.id,
                'date_order': fields.Datetime.now(),
                'pricelist_id': self.partner_id.property_product_pricelist.id,
            }
            quotation = self.env['sale.order'].create(quotation_vals)
            
            # Update the order
            self.write({
                'quotation_id': quotation.id,
                'state': 'processed',
                'last_update': fields.Datetime.now()
            })
            
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'res_id': quotation.id,
                'view_mode': 'form',
                'target': 'current',
            }
        except Exception as e:
            self.write({
                'state': 'error',
                'error_message': str(e),
                'last_update': fields.Datetime.now()
            })
            raise UserError(_('Error processing order: %s') % str(e))

    def action_reset(self):
        """Reset the order to new state."""
        self.ensure_one()
        if self.state != 'error':
            raise UserError(_('Only orders in error state can be reset.'))
        
        self.write({
            'state': 'new',
            'error_message': False,
            'last_update': fields.Datetime.now()
        }) 
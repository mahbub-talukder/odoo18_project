import logging
import requests
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class ApiConfig(models.Model):
    _name = 'unified.sales.api.config'
    _description = 'External API Configuration'

    name = fields.Char('Name', required=True)
    api_type = fields.Selection([
        ('shopify', 'Shopify'),
        ('woocommerce', 'WooCommerce'),
        ('custom', 'Custom API')
    ], string='API Type', required=True)
    
    api_url = fields.Char('API URL', required=True)
    api_key = fields.Char('API Key', required=True)
    api_secret = fields.Char('API Secret', required=True)
    webhook_url = fields.Char('Webhook URL', compute='_compute_webhook_url', readonly=True)
    active = fields.Boolean('Active', default=True)
    
    last_sync_date = fields.Datetime('Last Sync Date')
    
    @api.depends('api_type')
    def _compute_webhook_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for config in self:
            config.webhook_url = f"{base_url}/unified_sales/webhook/{config.id}"
    
    def test_connection(self):
        self.ensure_one()
        try:
            if self.api_type == 'shopify':
                # Example test connection for Shopify
                headers = {
                    'X-Shopify-Access-Token': self.api_secret,
                    'Content-Type': 'application/json'
                }
                response = requests.get(f"{self.api_url}/admin/api/2023-04/shop.json", headers=headers)
                response.raise_for_status()
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('Connection Successful'),
                        'message': _('Successfully connected to the API.'),
                        'sticky': False,
                        'type': 'success',
                    }
                }
            else:
                # Implement similar logic for other API types (Django backend)
                pass
        except Exception as e:
            _logger.error("API Connection Test Error: %s", str(e))
            raise UserError(_('Connection Test Failed: %s') % str(e))

class ExternalOrder(models.Model):
    _name = 'unified.sales.external.order'
    _description = 'External Order'
    _rec_name = 'external_id'
    
    external_id = fields.Char('External ID', required=True)
    api_config_id = fields.Many2one('unified.sales.api.config', string='API Config', required=True)
    
    partner_id = fields.Many2one('res.partner', string='Customer')
    quotation_id = fields.Many2one('sale.order', string='Quotation')
    
    date_created = fields.Datetime('Date Created')
    external_data = fields.Text('External Data')
    state = fields.Selection([
        ('new', 'New'),
        ('processed', 'Processed'),
        ('error', 'Error')
    ], string='Status', default='new')
    error_message = fields.Text('Error Message')
    
    _sql_constraints = [
        ('external_id_api_uniq', 'unique(external_id, api_config_id)', 'The external order ID must be unique per API configuration!')
    ] 
from odoo import api, fields, models, _
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)

class DjangoApiConfig(models.Model):
    _name = 'unified.sales.django.api'
    _description = 'Django API Configuration'

    name = fields.Char('Name', required=True)
    api_url = fields.Char('API URL', required=True)
    api_key = fields.Char('API Key', required=True)
    webhook_url = fields.Char('Webhook URL', compute='_compute_webhook_url', readonly=True)
    active = fields.Boolean('Active', default=True)
    last_sync_date = fields.Datetime('Last Sync Date')

    @api.depends('name')
    def _compute_webhook_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for config in self:
            config.webhook_url = f"{base_url}/api/v1/webhook/create-quotation"

    def test_connection(self):
        self.ensure_one()
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.get(f"{self.api_url}/api/products/", headers=headers)
            response.raise_for_status()
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Connection Successful'),
                    'message': _('Successfully connected to Django API.'),
                    'sticky': False,
                    'type': 'success',
                }
            }
        except Exception as e:
            _logger.error("Django API Connection Test Error: %s", str(e))
            raise UserError(_('Connection Test Failed: %s') % str(e))

    def sync_products(self):
        """Sync products from Django to Odoo"""
        self.ensure_one()
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.get(f"{self.api_url}/api/products/", headers=headers)
            response.raise_for_status()
            products = response.json()

            Product = self.env['product.product'].sudo()
            for product_data in products:
                # Check if product exists
                product = Product.search([
                    ('default_code', '=', product_data.get('sku'))
                ], limit=1)

                vals = {
                    'name': product_data.get('name'),
                    'default_code': product_data.get('sku'),
                    'list_price': float(product_data.get('price', 0.0)),
                    'type': 'product',
                    'sale_ok': True,
                    'purchase_ok': True,
                }

                if product:
                    product.write(vals)
                else:
                    Product.create(vals)

            self.write({'last_sync_date': fields.Datetime.now()})
            return True
        except Exception as e:
            _logger.error("Error syncing products: %s", str(e))
            raise UserError(_('Product Sync Failed: %s') % str(e))

    def create_purchase_order(self, order_data):
        """Create a purchase order in Django"""
        self.ensure_one()
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.post(
                f"{self.api_url}/api/purchase-orders/",
                json=order_data,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            _logger.error("Error creating purchase order: %s", str(e))
            raise UserError(_('Failed to create purchase order: %s') % str(e)) 
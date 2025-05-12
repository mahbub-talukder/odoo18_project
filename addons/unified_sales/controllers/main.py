import json
import logging
import werkzeug

from odoo import http, fields
from odoo.http import request

_logger = logging.getLogger(__name__)

class UnifiedSalesController(http.Controller):
    
    @http.route('/unified_sales/webhook/<int:api_config_id>', type='json', auth='public', csrf=False, methods=['POST'])
    def webhook_handler(self, api_config_id, **kwargs):
        """Handle webhooks from external APIs"""
        _logger.info("Webhook received for API config %s", api_config_id)
        
        try:
            # Get API configuration
            api_config = request.env['unified.sales.api.config'].sudo().browse(api_config_id)
            if not api_config.exists() or not api_config.active:
                _logger.warning("Invalid or inactive API configuration: %s", api_config_id)
                return werkzeug.exceptions.BadRequest("Invalid API configuration")
            
            # Get webhook payload
            data = request.jsonrequest
            _logger.debug("Webhook payload: %s", json.dumps(data))
            
            # Process based on API type
            if api_config.api_type == 'shopify':
                return self._process_shopify_webhook(api_config, data)
            elif api_config.api_type == 'woocommerce':
                return self._process_woocommerce_webhook(api_config, data)
            else:
                return self._process_custom_webhook(api_config, data)
                
        except Exception as e:
            _logger.exception("Error processing webhook: %s", str(e))
            return {'success': False, 'error': str(e)}
    
    def _process_shopify_webhook(self, api_config, data):
        """Process Shopify webhook data"""
        # Check if this is an order creation webhook
        if 'order_number' not in data:
            return {'success': False, 'message': 'Not an order webhook'}
        
        external_order_id = data.get('id') or data.get('order_id')
        if not external_order_id:
            return {'success': False, 'message': 'No order ID found'}
        
        # Check if we already have this order
        existing_order = request.env['unified.sales.external.order'].sudo().search([
            ('external_id', '=', str(external_order_id)),
            ('api_config_id', '=', api_config.id)
        ], limit=1)
        
        if existing_order:
            return {'success': True, 'message': 'Order already exists', 'order_id': existing_order.id}
        
        # Process the order
        return self._create_quotation_from_external_order(api_config, data, str(external_order_id))
    
    def _process_woocommerce_webhook(self, api_config, data):
        """Process WooCommerce webhook data"""
        # Similar to Shopify but with WooCommerce structure
        if 'id' not in data:
            return {'success': False, 'message': 'No order ID found'}
        
        external_order_id = str(data.get('id'))
        
        # Check if we already have this order
        existing_order = request.env['unified.sales.external.order'].sudo().search([
            ('external_id', '=', external_order_id),
            ('api_config_id', '=', api_config.id)
        ], limit=1)
        
        if existing_order:
            return {'success': True, 'message': 'Order already exists', 'order_id': existing_order.id}
        
        # Process the order
        return self._create_quotation_from_external_order(api_config, data, external_order_id)
    
    def _process_custom_webhook(self, api_config, data):
        """Process custom API webhook data"""
        # Implement based on your custom API structure
        return {'success': True, 'message': 'Custom webhook processed'}
    
    def _create_quotation_from_external_order(self, api_config, data, external_order_id):
        """Create a quotation from external order data"""
        try:
            # Create external order record
            external_order = request.env['unified.sales.external.order'].sudo().create({
                'external_id': external_order_id,
                'api_config_id': api_config.id,
                'date_created': data.get('created_at') or fields.Datetime.now(),
                'external_data': json.dumps(data),
                'state': 'new',
            })
            
            # Process customer information
            customer_data = None
            if api_config.api_type == 'shopify':
                customer_data = data.get('customer', {})
            elif api_config.api_type == 'woocommerce':
                customer_data = data.get('billing', {})
            
            if not customer_data:
                external_order.write({'state': 'error', 'error_message': 'No customer data found'})
                return {'success': False, 'message': 'No customer data found'}
            
            # Find or create partner
            partner = self._find_or_create_partner(customer_data, api_config.api_type)
            if not partner:
                external_order.write({'state': 'error', 'error_message': 'Could not create customer'})
                return {'success': False, 'message': 'Could not create customer'}
            
            external_order.write({'partner_id': partner.id})
            
            # Create quotation
            quotation = request.env['sale.order'].sudo().create({
                'partner_id': partner.id,
                'state': 'draft',
                'client_order_ref': external_order_id,
            })
            
            # Add order lines
            self._add_order_lines(quotation, data, api_config.api_type)
            
            # Link quotation to external order
            external_order.write({
                'quotation_id': quotation.id,
                'state': 'processed'
            })
            
            return {
                'success': True,
                'message': 'Quotation created successfully',
                'quotation_id': quotation.id,
                'external_order_id': external_order.id
            }
            
        except Exception as e:
            _logger.exception("Error creating quotation: %s", str(e))
            if external_order:
                external_order.write({'state': 'error', 'error_message': str(e)})
            return {'success': False, 'error': str(e)}
    
    def _find_or_create_partner(self, customer_data, api_type):
        """Find or create a partner based on customer data"""
        Partner = request.env['res.partner'].sudo()
        
        email = None
        name = None
        
        if api_type == 'shopify':
            email = customer_data.get('email')
            name = customer_data.get('first_name', '') + ' ' + customer_data.get('last_name', '')
        elif api_type == 'woocommerce':
            email = customer_data.get('email')
            name = customer_data.get('first_name', '') + ' ' + customer_data.get('last_name', '')
        
        if not email or not name:
            return False
        
        # Search for existing partner
        partner = Partner.search([('email', '=', email)], limit=1)
        if partner:
            return partner
        
        # Create new partner
        vals = {
            'name': name,
            'email': email,
            'customer_rank': 1,
        }
        
        # Add address information if available
        if api_type == 'shopify' and 'default_address' in customer_data:
            address = customer_data['default_address']
            vals.update({
                'phone': address.get('phone'),
                'street': address.get('address1'),
                'street2': address.get('address2'),
                'city': address.get('city'),
                'zip': address.get('zip'),
                'country_id': self._get_country_id(address.get('country_code')),
            })
        elif api_type == 'woocommerce':
            vals.update({
                'phone': customer_data.get('phone'),
                'street': customer_data.get('address_1'),
                'street2': customer_data.get('address_2'),
                'city': customer_data.get('city'),
                'zip': customer_data.get('postcode'),
                'country_id': self._get_country_id(customer_data.get('country')),
            })
        
        return Partner.create(vals)
    
    def _get_country_id(self, country_code):
        """Get country ID from country code"""
        if not country_code:
            return False
            
        country = request.env['res.country'].sudo().search([
            '|', ('code', '=', country_code), ('name', '=', country_code)
        ], limit=1)
        
        return country.id if country else False
    
    def _add_order_lines(self, quotation, data, api_type):
        """Add order lines to quotation"""
        SaleOrderLine = request.env['sale.order.line'].sudo()
        Product = request.env['product.product'].sudo()
        
        items = []
        if api_type == 'shopify':
            items = data.get('line_items', [])
        elif api_type == 'woocommerce':
            items = data.get('line_items', [])
        
        for item in items:
            # Try to find product by SKU or create a generic one
            product_code = None
            if api_type == 'shopify':
                product_code = item.get('sku') or item.get('product_id')
            elif api_type == 'woocommerce':
                product_code = item.get('sku')
            
            product = False
            if product_code:
                product = Product.search([('default_code', '=', product_code)], limit=1)
            
            if not product:
                # Use a default product or create a generic one
                product = Product.search([('default_code', '=', 'GENERIC')], limit=1)
                
                if not product:
                    # Create a generic product
                    product = Product.create({
                        'name': 'Generic Product',
                        'default_code': 'GENERIC',
                        'type': 'product',
                        'sale_ok': True,
                        'purchase_ok': True,
                    })
            
            # Create order line
            name = None
            quantity = None
            price_unit = None
            
            if api_type == 'shopify':
                name = item.get('name', 'Unknown Product')
                quantity = item.get('quantity', 1)
                price_unit = item.get('price', 0.0)
            elif api_type == 'woocommerce':
                name = item.get('name', 'Unknown Product')
                quantity = item.get('quantity', 1)
                price_unit = item.get('price', 0.0)
            
            SaleOrderLine.create({
                'order_id': quotation.id,
                'product_id': product.id,
                'name': name,
                'product_uom_qty': quantity,
                'price_unit': price_unit,
            }) 
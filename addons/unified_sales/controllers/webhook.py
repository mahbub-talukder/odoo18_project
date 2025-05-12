from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

class WebhookController(http.Controller):
    @http.route('/api/v1/webhook/create-quotation', type='http', auth='public', methods=['POST'], csrf=False)
    def create_quotation(self, **kwargs):
        try:
            # Get JSON data from request
            data = json.loads(request.httprequest.data)
            _logger.info("Received webhook data: %s", data)

            # Check if VAT should be included (default: False)
            tax_included = data.get('tax_included', False)
            
            # Find or create partner
            partner = request.env['res.partner'].sudo().search([
                '|',
                ('email', '=', data.get('email')),
                ('phone', '=', data.get('phone'))
            ], limit=1)

            if not partner:
                partner = request.env['res.partner'].sudo().create({
                    'name': data.get('partner_name'),
                    'email': data.get('email'),
                    'phone': data.get('phone'),
                    'street': data.get('shipping_address'),
                })

            # Find the default 15% tax if tax_included is True
            tax_id = False
            if tax_included:
                tax = request.env['account.tax'].sudo().search([
                    ('amount', '=', 15),
                    ('type_tax_use', '=', 'sale'),
                    ('amount_type', '=', 'percent')
                ], limit=1)
                if tax:
                    tax_id = tax.id
                    _logger.info("Found 15% VAT tax: %s", tax.name)
                else:
                    _logger.warning("15% VAT tax not found in the system")

            # Process order lines
            order_lines = []
            for line in data.get('order_lines', []):
                # Try to find the product by name
                product = request.env['product.product'].sudo().search([
                    ('name', '=', line.get('product_name'))
                ], limit=1)

                if not product:
                    # Create product template first
                    template = request.env['product.template'].sudo().create({
                        'name': line.get('product_name'),
                        'type': 'consu',  # Changed to 'consu' for consumable products
                        'list_price': float(line.get('price_unit', 0.0)),
                        'default_code': f"EXT-{line.get('product_name')[:8].upper()}",  # Generate a code
                        'sale_ok': True,
                    })
                    
                    # Get the product variant
                    product = template.product_variant_id
                    _logger.info("Created new product: %s", product.name)

                # Prepare the order line values
                line_vals = {
                    'product_id': product.id,
                    'name': product.name,
                    'product_uom_qty': float(line.get('quantity', 1.0)),
                    'price_unit': float(line.get('price_unit', 0.0)),
                }
                
                # Add tax if tax_included is True and tax exists
                if tax_included and tax_id:
                    line_vals['tax_id'] = [(6, 0, [tax_id])]

                # Create order line
                order_lines.append((0, 0, line_vals))

            # Create quotation
            quotation = request.env['sale.order'].sudo().create({
                'partner_id': partner.id,
                'client_order_ref': data.get('name') or f"PO-{partner.id}",
                'order_line': order_lines
            })

            _logger.info("Created quotation: %s", quotation.name)
            
            response_data = {
                'status': 'success',
                'quotation_id': quotation.id,
                'quotation_name': quotation.name,
                'created_products': [p.name for p in request.env['product.product'].sudo().search([
                    ('name', 'in', [line.get('product_name') for line in data.get('order_lines', [])])
                ])],
                'tax_included': tax_included
            }
            
            return http.Response(
                json.dumps(response_data),
                content_type='application/json',
                status=200
            )

        except json.JSONDecodeError as e:
            _logger.error("Invalid JSON data received: %s", str(e))
            return http.Response(
                json.dumps({
                    'status': 'error',
                    'message': 'Invalid JSON data'
                }),
                content_type='application/json',
                status=400
            )
        except Exception as e:
            _logger.error("Error in webhook: %s", str(e))
            return http.Response(
                json.dumps({
                    'status': 'error',
                    'message': str(e)
                }),
                content_type='application/json',
                status=500
            ) 
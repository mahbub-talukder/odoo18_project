from odoo import models
import logging

_logger = logging.getLogger(__name__)

class WebsiteController(models.AbstractModel):
    _inherit = 'website'

    def _get_product_seo_data(self, product_template_id, website_id):
        """Get website-specific SEO data for a product"""
        ProductSEO = self.env['product.template.seo']
        domain = [
            ('product_tmpl_id', '=', product_template_id),
            ('website_id', '=', website_id)
        ]
        product_seo = ProductSEO.search(domain, limit=1)
        if not product_seo:
            # No website-specific data found, create a new record
            product = self.env['product.template'].browse(product_template_id)
            vals = {
                'product_tmpl_id': product_template_id,
                'website_id': website_id,
                'website_meta_title': product.website_meta_title or '',
                'website_meta_description': product.website_meta_description or '',
                'website_meta_keywords': product.website_meta_keywords or '',
                'website_meta_og_img': product.website_meta_og_img or '',
                'seo_name': product.seo_name or '',
            }
            try:
                product_seo = ProductSEO.sudo().create(vals)
                _logger.info(f"Created website-specific SEO data for product: {product_seo.id}")
            except Exception as e:
                _logger.error(f"Error creating website-specific SEO data: {str(e)}")
                return None
        
        return product_seo
    
    def get_website_meta(self, template_values):
        """Override to include website-specific SEO data for products"""
        res = super(WebsiteController, self).get_website_meta(template_values)
        
        product = template_values.get('product')
        if product and product._name == 'product.template':
            # Get the current website
            website = self.get_current_website()
            _logger.info(f"Getting SEO data for product {product.id} on website {website.id}")
            
            # Get website-specific SEO data
            product_seo = self._get_product_seo_data(product.id, website.id)
            if product_seo:
                _logger.info(f"Found website-specific SEO data for product: {product_seo.id}")
                
                # Override SEO fields with website-specific values
                if product_seo.website_meta_title:
                    res['website_meta_title'] = product_seo.website_meta_title
                if product_seo.website_meta_description:
                    res['website_meta_description'] = product_seo.website_meta_description
                if product_seo.website_meta_keywords:
                    res['website_meta_keywords'] = product_seo.website_meta_keywords
                if product_seo.website_meta_og_img:
                    res['website_meta_og_img'] = product_seo.website_meta_og_img
                    
                _logger.info(f"Applied website-specific SEO data: {res}")
        
        return res 
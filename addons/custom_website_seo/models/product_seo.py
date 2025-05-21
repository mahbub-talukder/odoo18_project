from odoo import api, fields, models, _

class ProductTemplateSEO(models.Model):
    _name = 'product.template.seo'
    _description = 'Website-specific SEO data for products'
    
    product_tmpl_id = fields.Many2one('product.template', required=True, ondelete='cascade', 
                                     string="Product Template")
    website_id = fields.Many2one('website', required=True, ondelete='cascade',
                                string="Website")
    website_meta_title = fields.Char("Website Meta Title")
    website_meta_description = fields.Text("Website Meta Description")
    website_meta_keywords = fields.Char("Website Meta Keywords")
    website_meta_og_img = fields.Char("Website OG Image")
    seo_name = fields.Char("SEO URL")
    
    _sql_constraints = [
        ('unique_product_website', 'unique(product_tmpl_id, website_id)', 
         'You can only have one SEO configuration per product per website!')
    ]
    
    @api.model
    def get_for_product(self, product_id, website_id):
        """Get or create website-specific SEO data for a product"""
        domain = [
            ('product_tmpl_id', '=', product_id),
            ('website_id', '=', website_id)
        ]
        product_seo = self.search(domain, limit=1)
        if not product_seo:
            # Get default values from product
            product = self.env['product.template'].browse(product_id)
            vals = {
                'product_tmpl_id': product_id,
                'website_id': website_id,
                'website_meta_title': product.website_meta_title,
                'website_meta_description': product.website_meta_description,
                'website_meta_keywords': product.website_meta_keywords,
                'website_meta_og_img': product.website_meta_og_img,
                'seo_name': product.seo_name,
            }
            product_seo = self.create(vals)
        return product_seo 
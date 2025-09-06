from odoo import models, fields, api


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    tag_ids = fields.Many2many(
        'ox.pricelist.tag',
        'pricelist_tag_rel',
        'pricelist_id',
        'tag_id',
        string='Tags',
        help='Tags associated with this pricelist'
    )
    
    @api.model
    def get_portal_user_pricelist_tags(self, partner_id=None):
        """
        Get tags for the pricelist assigned to a portal user
        This method can be called from website templates
        Odoo 18 compatible implementation
        """
        if not partner_id:
            # Try to get from current user
            if hasattr(self.env.user, 'partner_id') and self.env.user.partner_id:
                partner_id = self.env.user.partner_id.id
            else:
                return self.env['ox.pricelist.tag']
        
        partner = self.env['res.partner'].browse(partner_id)
        if not partner.property_product_pricelist:
            return self.env['ox.pricelist.tag']
        
        return partner.property_product_pricelist.tag_ids.filtered('active')

    @api.model
    def _get_portal_tags_for_website(self):
        """
        Optimized method for website template usage
        Returns active tags for current user's pricelist
        """
        if not self.env.user._is_public():
            return self.get_portal_user_pricelist_tags()
        return self.env['ox.pricelist.tag']

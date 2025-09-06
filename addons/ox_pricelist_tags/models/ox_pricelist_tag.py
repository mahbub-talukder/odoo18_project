from odoo import models, fields, api


class OxPricelistTag(models.Model):
    _name = 'ox.pricelist.tag'
    _description = 'OX Pricelist Tag'
    _order = 'name'

    name = fields.Char(
        string='Tag Name',
        required=True,
        translate=True,
        help='Name of the pricelist tag'
    )
    
    color = fields.Integer(
        string='Color Index',
        default=0,
        help='Color index (0-11) for kanban and tag display'
    )
    
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Set to false to hide the tag without removing it'
    )
    
    pricelist_ids = fields.Many2many(
        'product.pricelist',
        'pricelist_tag_rel',
        'tag_id',
        'pricelist_id',
        string='Pricelists',
        help='Pricelists using this tag'
    )
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The tag name must be unique!'),
    ]

    def name_get(self):
        """Override name_get to show tag name only"""
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result

    def toggle_active(self):
        """Toggle active status - Odoo 18 compatible"""
        for record in self:
            record.active = not record.active
        return True

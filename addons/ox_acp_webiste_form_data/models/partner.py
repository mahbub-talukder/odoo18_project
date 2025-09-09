# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_studio_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    profession = fields.Char(string='Profession')
    place_of_birth = fields.Char(string='Place of Birth')
    date_of_birth = fields.Date(string='Date of Birth')


    def create_user(self, login=None, password=None, **user_vals):
        """Create a user for this partner instance"""
        self.ensure_one()
        
        # Check if user already exists for this partner
        existing_user = self.env['res.users'].search([('partner_id', '=', self.id)], limit=1)
        if existing_user:
            raise UserError(f"User already exists for partner {self.name}")
        
        # Prepare user values
        vals = {
            'partner_id': self.id,
            'login': login or self.email,
            'password': password or 'default123',  # You should generate a proper password
            'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],  # Default to portal user
        }
        vals.update(user_vals)
        
        # Validate login is provided
        if not vals.get('login'):
            raise UserError("Login is required to create a user")
            
        return self.env['res.users'].create(vals)
    
    def find_user(self):
        """Find user associated with this partner instance"""
        self.ensure_one()
        return self.env['res.users'].search([('partner_id', '=', self.id)], limit=1)
    
    def create_or_find_user(self, login=None, password=None, **user_vals):
        """Find existing user or create new one for this partner"""
        self.ensure_one()
        
        # First try to find existing user
        user = self.find_user()
        
        if user:
            return user, False  # Return user and False (not created)
        
        # Create new user if not found
        user = self.create_user(login=login, password=password, **user_vals)
        return user, True  # Return user and True (created)
    
    def ensure_user_exists(self, **user_vals):
        """Ensure user exists for this partner, create if needed"""
        user = self.find_user()
        if not user:
            user = self.create_user(**user_vals)
        return user
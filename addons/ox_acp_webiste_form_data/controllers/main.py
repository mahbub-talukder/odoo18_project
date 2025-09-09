# -*- coding: utf-8 -*-

import random
from odoo import http
from odoo.exceptions import UserError

from odoo.http import request
import json
import logging
logger = logging.getLogger(__name__)
RESPONSE_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Methods': 'POST, OPTIONS, GET, PUT, DELETE',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': 'true'
}

class WebsiteFormController(http.Controller):
    @http.route('/api/get_countries', type='http',website=False, auth='public', methods=['GET'], csrf=False)
    def get_countries(self, **kw):
        countries = request.env['res.country'].sudo().search_read([], ['id', 'name'])
        return request.make_response(json.dumps(countries), headers=RESPONSE_HEADERS)
    
    @http.route('/api/submit_form',  auth='public', website=False, type='http', method=["POST","OPTIONS"], csrf=False)
    def submit_form(self, **kwargs):
        try:
            
            if request.httprequest.method == 'OPTIONS':
                logger.info("OPTIONS request received")
                return request.make_response('', headers=RESPONSE_HEADERS)
            
            print("POST request received")
            logger.info("POST request received")
            logger.info(kwargs)
            post = json.loads(request.httprequest.data.decode('utf-8'))
            logger.info('data')
            logger.info(post)

            logger.info("============")
            # 1. Server-side validation
            required_fields = ['full_name', 'email', 'phone', 'x_studio_gender', 'profession', 'place_of_birth', 'nationality_id', 'date_of_birth']
            for field in required_fields:
                if not post.get(field):
                    return request.make_response(json.dumps({'error': 'Missing required field: %s' % field}), headers=RESPONSE_HEADERS)

            # 2. Already Registered Email Validation
            existing_partner = request.env['res.partner'].sudo().search([('email', '=', post.get('email'))], limit=1)
            if existing_partner:
                return request.make_response(json.dumps({'error': 'This email address is already registered. Please use the Membership Portal to log in or reset your password.'}), headers=RESPONSE_HEADERS)

            try:
                # 3. Create a new record in res.partner
                partner_vals = {
                    'name': post.get('full_name'),
                    'email': post.get('email'),
                    'phone': post.get('phone'),
                    'x_studio_gender': post.get('x_studio_gender'),
                    'profession': post.get('profession'),
                    'place_of_birth': post.get('place_of_birth'),
                    'country_id': int(post.get('nationality_id')),
                    'date_of_birth': post.get('date_of_birth'),
                }
                new_partner = request.env['res.partner'].sudo().create(partner_vals)
                logger.info(f"Created partner: {new_partner.id}")

                # 4. Create portal user using proper Odoo portal invitation process
                if new_partner:
                    # Method 1: Use portal wizard (Recommended)
                    portal_wizard = request.env['portal.wizard'].sudo().create({
                        'partner_ids': [(6, 0, [new_partner.id])]
                    })
                    
                    # Get the wizard user record
                    wizard_user = portal_wizard.user_ids.filtered(lambda u: u.partner_id.id == new_partner.id)
                    
                    if wizard_user:
                        # Send portal invitation
                        wizard_user.action_grant_access()
                        logger.info(f"Portal access granted to partner: {new_partner.id}")
                        
                        # Check if user was created
                        portal_user = request.env['res.users'].sudo().search([('partner_id', '=', new_partner.id)], limit=1)
                        if portal_user:
                            logger.info(f"Portal user created: {portal_user.login}")
                        else:
                            logger.warning(f"Portal user not found after invitation for partner: {new_partner.id}")
                    else:
                        logger.error(f"Could not create portal wizard user for partner: {new_partner.id}")
                        raise UserError("Could not create portal access")

                # 5. Retrieve membership number (assuming 'id_number' exists)
                try:
                    membership_number = getattr(new_partner, 'id_number', None) or f"MEM-{new_partner.id:06d}"
                except Exception as e:
                    logger.error(f"Error getting membership number: {str(e)}")
                    membership_number = f"MEM-{new_partner.id:06d}"

                # 6. Success response
                return request.make_response(json.dumps({
                    'success': True,
                    'message': f'Your membership number is: {membership_number}. Please check your email for portal access instructions.',
                    'membership_number': membership_number
                }), headers=RESPONSE_HEADERS)

            except Exception as e:
                logger.error(f"Error creating partner/user: {str(e)}")
                # 7. Error response for other issues
                return request.make_response(json.dumps({'error': str(e)}), headers=RESPONSE_HEADERS)
                
        except Exception as e:
            logger.error(f"General error: {str(e)}")
            return request.make_response(json.dumps({
                'error': str(e),
                'success': False,
                'message': 'An unexpected error occurred. Please try again.'
            }), headers=RESPONSE_HEADERS)
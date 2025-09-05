# -*- coding: utf-8 -*-
from odoo import models, api

class ShopifyResPartnerEpt(models.Model):
    _inherit = "shopify.res.partner.ept"

    @api.model
    def shopify_create_contact_partner(self, vals, instance, queue_line):
        """
        Override the original method to check for existing contacts by email first
        before creating a new contact.
        """
        partner_obj = self.env["res.partner"]
        common_log_line_obj = self.env["common.log.lines.ept"]

        shopify_instance_id = instance.id
        shopify_customer_id = vals.get("id", False)
        first_name = vals.get("first_name", "")
        last_name = vals.get("last_name", "")
        email = vals.get("email", "")
        
        if not first_name and not last_name and not email:
            message = "First name, Last name and Email are not found in customer data."
            common_log_line_obj.create_common_log_line_ept(shopify_instance_id=instance.id, module="shopify_ept",
                                                           message=message,
                                                           model_name='res.partner',
                                                           shopify_order_data_queue_line_id=queue_line.id if self._context.get(
                                                               'order_data_queue') else False,
                                                           shopify_customer_data_queue_line_id=queue_line.id if self._context.get(
                                                               'customer_data_queue') else False,
                                                           order_ref=queue_line.shopify_order_id if self._context.get(
                                                               'order_data_queue') else False)
            return False

        name = ""
        if first_name:
            name = "%s" % first_name
        if last_name:
            name += " %s" % last_name if name else "%s" % last_name
        if not name and email:
            name = email

        # First check if a partner exists with this email
        if email:
            existing_partner = partner_obj.search([('email', '=', email)], limit=1)
            if existing_partner:
                # Check if there's already a Shopify partner record
                shopify_partner = self.search([
                    ('shopify_customer_id', '=', shopify_customer_id),
                    ('shopify_instance_id', '=', shopify_instance_id)
                ], limit=1)
                
                if not shopify_partner:
                    # Create Shopify partner record if it doesn't exist
                    self.create({
                        'shopify_customer_id': shopify_customer_id,
                        'shopify_instance_id': shopify_instance_id,
                        'partner_id': existing_partner.id
                    })
                
                # Update partner tags if any
                tags = vals.get("tags").split(",") if vals.get("tags") != '' else vals.get("tags")
                tag_ids = []
                for tag in tags:
                    tag_ids.append(partner_obj.create_or_search_tag(tag))
                
                if tag_ids:
                    existing_partner.write({
                        'is_shopify_customer': True,
                        'category_id': [(6, 0, tag_ids)]
                    })
                
                return existing_partner

        # If no existing partner found by email, proceed with original logic
        partner = self.search_shopify_partner(shopify_customer_id, shopify_instance_id)
        tags = vals.get("tags").split(",") if vals.get("tags") != '' else vals.get("tags")
        tag_ids = []
        for tag in tags:
            tag_ids.append(partner_obj.create_or_search_tag(tag))

        if partner:
            if not partner.parent_id:
                partner = self.update_partner_with_company(instance, vals.get("default_address", {}), False, partner)
            partner.write({"category_id": [(6, 0, tag_ids)]})
            return partner

        shopify_partner_values = {
            "shopify_customer_id": shopify_customer_id,
            "shopify_instance_id": shopify_instance_id
        }

        partner_vals = self.shopify_prepare_partner_vals(vals.get("default_address", {}), instance)
        partner_vals.update({
            "name": name,
            "email": email,
            "customer_rank": 1,
            "is_shopify_customer": True,
            "type": "contact",
            "category_id": [(6, 0, tag_ids)],
            "phone": vals.get("phone", "") if not partner_vals.get("phone") else partner_vals.get("phone")
        })
        partner = partner_obj.create(partner_vals)

        shopify_partner_values.update({"partner_id": partner.id})
        self.create(shopify_partner_values)
        partner = self.update_partner_with_company(instance, vals.get("default_address", {}), False, partner)
        return partner 
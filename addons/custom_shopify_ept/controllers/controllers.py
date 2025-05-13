# -*- coding: utf-8 -*-
# from odoo import http


# class ./customAdon/customShopifyEpt(http.Controller):
#     @http.route('/./custom_adon/custom_shopify_ept/./custom_adon/custom_shopify_ept', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./custom_adon/custom_shopify_ept/./custom_adon/custom_shopify_ept/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./custom_adon/custom_shopify_ept.listing', {
#             'root': '/./custom_adon/custom_shopify_ept/./custom_adon/custom_shopify_ept',
#             'objects': http.request.env['./custom_adon/custom_shopify_ept../custom_adon/custom_shopify_ept'].search([]),
#         })

#     @http.route('/./custom_adon/custom_shopify_ept/./custom_adon/custom_shopify_ept/objects/<model("./custom_adon/custom_shopify_ept../custom_adon/custom_shopify_ept"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./custom_adon/custom_shopify_ept.object', {
#             'object': obj
#         })


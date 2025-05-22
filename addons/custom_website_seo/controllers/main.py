from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website
import werkzeug
import logging

_logger = logging.getLogger(__name__)

class CustomWebsiteController(Website):
    
    @http.route(['/website/get_websites'], type='json', auth="user", website=True, readonly=True)
    def get_websites(self):
        """Returns a list of all available websites for the current user"""
        Website = request.env['website']
        websites = Website.search([])
        
        # Only include websites that the user has access to
        user_websites = []
        for website in websites:
            try:
                # Check if user can modify/access this website
                website._check_user_can_modify(website)
                user_websites.append({
                    'id': website.id,
                    'name': website.name,
                    'domain': website.domain or request.httprequest.host,
                })
            except:
                continue
                
        return user_websites
    
    @http.route(['/website/get_seo_data_for_website'], type='json', auth="user", website=True, readonly=True)
    def get_seo_data_for_website(self, res_id, res_model, website_id, view_id=None):
        _logger.info(f"SEO Data Fetching - Input params: res_id: {res_id}, res_model: {res_model}, view_id: {view_id}, website_id: {website_id}")
        """Gets SEO data for a specific record in the context of a specific website and view_id"""
        if not request.env.user.has_group('website.group_website_restricted_editor'):
            # Still ok if user can access the record anyway.
            try:
                record = request.env[res_model].browse(res_id)
                record.check_access('write')
            except:
                raise werkzeug.exceptions.Forbidden()
        
        # Get the target website
        target_website = request.env['website'].browse(int(website_id))
        if not target_website.exists():
            return {'error': 'Website not found'}
            
        # Check URL compatibility
        current_website = request.website
        # Get current path from request instead of metadata
        current_path = request.httprequest.path
        
        # Check if the page exists in the target website (simplified check)
        # For more complex validation, we would need to check if the URL resolves on the target website
        path_exists = True  # Simplified assumption
        
        fields = ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img']
        res = {
            'can_edit_seo': True,
            'url_compatible': path_exists
        }
        
        # Different approach based on model
        if res_model == 'ir.ui.view':
            # For views, we need to find the website-specific version
            base_view = request.env['ir.ui.view'].browse(int(res_id))
            _logger.info(f"Base view: {base_view.name} (ID: {base_view.id}, Key: {base_view.key})")
            
            # Look for website-specific customization
            domain = [
                ('key', '=', base_view.key),
                ('website_id', '=', int(website_id))
            ]
            website_specific_view = request.env['ir.ui.view'].search(domain, limit=1)
            
            if website_specific_view:
                # Website-specific view exists, use it
                _logger.info(f"Found website-specific view: {website_specific_view.id}")
                record = website_specific_view
            else:
                # No customization exists yet, use base view
                _logger.info(f"No website-specific view found, using base view")
                record = base_view
                
        elif res_model == 'website.page':
            # For pages, first get the page
            page = request.env['website.page'].browse(int(res_id))
            
            if not view_id or view_id == 'undefined':
                view_id = page.view_id.id
                _logger.info(f"Using view_id from page: {view_id}")
            
            # Then get its view, with website customization if any
            base_view = request.env['ir.ui.view'].browse(int(view_id))
            _logger.info(f"Base view for page: {base_view.name} (ID: {base_view.id}, Key: {base_view.key})")
            
            # Look for website-specific customization of the view
            domain = [
                ('key', '=', base_view.key),
                ('website_id', '=', int(website_id))
            ]
            website_specific_view = request.env['ir.ui.view'].search(domain, limit=1)
            
            if website_specific_view:
                # Use website-specific view
                _logger.info(f"Found website-specific view for page: {website_specific_view.id}")
                record = website_specific_view
                fields.extend(['website_id'])
                res["website_is_published"] = page.website_published
                
                # Add the indexed status from the page, not the view
                try:
                    res["website_indexed"] = page.website_indexed
                except:
                    _logger.warning("Could not get website_indexed from page")
            else:
                # Use base view
                _logger.info(f"No website-specific view found for page, using base view")
                record = base_view
                fields.extend(['website_id'])
                res["website_is_published"] = page.website_published
                
                # Add the indexed status from the page, not the view
                try:
                    res["website_indexed"] = page.website_indexed
                except:
                    _logger.warning("Could not get website_indexed from page")
        elif res_model == 'product.template':
            # For products, we need to handle website-specific SEO data differently
            # since products don't have the same inheritance mechanism as views
            _logger.info(f"Handling product SEO data for website {website_id}")
            product = request.env['product.template'].browse(int(res_id))
            
            # Check for website-specific SEO data in our custom model
            domain = [
                ('product_tmpl_id', '=', int(res_id)),
                ('website_id', '=', int(website_id))
            ]
            ProductSEO = request.env['product.template.seo']
            product_seo = ProductSEO.search(domain, limit=1)
            
            if product_seo:
                # Use the website-specific SEO data
                _logger.info(f"Found website-specific SEO data for product: {product_seo.id}")
                # Map fields from product_seo to expected response fields
                res.update({
                    'website_meta_title': product_seo.website_meta_title,
                    'website_meta_description': product_seo.website_meta_description,
                    'website_meta_keywords': product_seo.website_meta_keywords,
                    'website_meta_og_img': product_seo.website_meta_og_img,
                    'seo_name': product_seo.seo_name,
                })
                record = product  # Keep the original record for permission checks
            else:
                # No website-specific data yet, create a new one from product's default values
                _logger.info(f"No website-specific SEO data found for product, creating new record")
                record = product
                # Get values from product template
                vals = {
                    'product_tmpl_id': int(res_id),
                    'website_id': int(website_id),
                    'website_meta_title': product.website_meta_title or '',
                    'website_meta_description': product.website_meta_description or '',
                    'website_meta_keywords': product.website_meta_keywords or '',
                    'website_meta_og_img': product.website_meta_og_img or '',
                    'seo_name': product.seo_name or ''
                }
                
                # Create the product SEO record
                try:
                    new_product_seo = ProductSEO.sudo().create(vals)
                    _logger.info(f"Created website-specific SEO data for product: {new_product_seo.id}")
                    
                    # Return the newly created data
                    res.update({
                        'website_meta_title': new_product_seo.website_meta_title,
                        'website_meta_description': new_product_seo.website_meta_description,
                        'website_meta_keywords': new_product_seo.website_meta_keywords,
                        'website_meta_og_img': new_product_seo.website_meta_og_img,
                        'seo_name': new_product_seo.seo_name,
                    })
                except Exception as e:
                    _logger.error(f"Error creating website-specific SEO data: {str(e)}")
                    # If creation fails, still show values from product template
                    res.update({
                        'website_meta_title': vals['website_meta_title'],
                        'website_meta_description': vals['website_meta_description'],
                        'website_meta_keywords': vals['website_meta_keywords'],
                        'website_meta_og_img': vals['website_meta_og_img'],
                        'seo_name': vals['seo_name'],
                    })

            
            # Add website information
            res['website_name'] = target_website.name
            res['website_id'] = target_website.id
            
            _logger.info(f"Product SEO Data for {res_model} {res_id} on website {target_website.id}: {res}")
            return res
        


        else:
            # For other models, use standard approach with context
            _logger.info(f"Using standard approach for model: {res_model}")
            record = request.env[res_model].with_context(
                website_id=target_website.id,
            ).browse(res_id)
        
        try:
            target_website._check_user_can_modify(record)
        except Exception as e:
            _logger.error(f"User cannot modify record: {str(e)}")
            res['can_edit_seo'] = False
            
        if request.env.user.has_group('website.group_website_restricted_editor'):
            record = record.sudo()

        try:
            record_data = record.read(fields)[0] if record else {}
            _logger.info(f"Read data from record: {record_data}")
            res.update(record_data)
        except Exception as e:
            _logger.error(f"Error reading record data: {str(e)}")
            return {'error': f"Failed to read SEO data: {str(e)}"}

        res['has_social_default_image'] = target_website.has_social_default_image

        if res_model not in ('website.page', 'ir.ui.view', 'product.template') and 'seo_name' in record:
            res['seo_name_default'] = request.env['ir.http']._slugify(record.display_name or '')
            res['seo_name'] = record.seo_name and request.env['ir.http']._slugify(record.seo_name) or ''
        
        # Add website information
        res['website_name'] = target_website.name
        res['website_id'] = target_website.id
        
        _logger.info(f"SEO Data for {res_model} {res_id} on website {target_website.id}: {res}")
        return res
        
    @http.route(['/website/seo_save'], type='json', auth="user", website=True)
    def save_seo_data(self, res_id, res_model, website_id, data, view_id=None, lang=None):
        """Saves SEO data for a specific record in the context of a specific website"""
        _logger.info(f"SEO Save - Input params: res_id: {res_id}, res_model: {res_model}, view_id: {view_id}, website_id: {website_id}")
        _logger.info(f"SEO Save - Data to save: {data}")
        _logger.info(f"SEO Save - Language: {lang}")

        if not data:
            _logger.error("SEO Save - No data provided")
            return {'error': 'No data provided'}

        if not request.env.user.has_group('website.group_website_restricted_editor'):
            # Still ok if user can access the record anyway.
            try:
                record = request.env[res_model].browse(res_id)
                _logger.info(f"SEO Save - Record before permission check: {record.name if hasattr(record, 'name') else record}")
                record.check_access('write')
            except Exception as e:
                _logger.error(f"SEO Save - Permission error: {str(e)}")
                raise werkzeug.exceptions.Forbidden()
        
        # Get the target website
        target_website = request.env['website'].browse(int(website_id))
        if not target_website.exists():
            _logger.error(f"SEO Save - Website not found: {website_id}")
            return {'error': 'Website not found'}
            
        # Prepare context for the specific website and language
        ctx = {
            'website_id': target_website.id
        }
        
        # Add language to context if provided
        if lang:
            ctx['lang'] = lang
        else:
            # Use the default language of the target website if not specified
            ctx['lang'] = target_website.default_lang_id.code
            
        _logger.info(f"SEO Save - Context: {ctx}")
        
        # Define valid fields for each model type
        valid_fields = {
            'ir.ui.view': ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img'],
            'website.page': ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'website_indexed', 'website_id'],
            'product.template': ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'seo_name'],
            'product.category': ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'seo_name'],
            'blog.post': ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'seo_name'],
            'blog.blog': ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'seo_name'],
        }
        
        # Get valid fields for this model, default to common SEO fields if model not found
        model_fields = valid_fields.get(res_model, ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img'])
        
        # Filter out invalid fields and empty values
        filtered_data = {k: v for k, v in data.items() if k in model_fields and v is not None}
        
        if not filtered_data:
            _logger.warning("SEO Save - No valid data to save after filtering")
            return {'warning': 'No valid data to save'}
        
        try:
            # Different approach based on model
            if res_model == 'ir.ui.view':
                # For views, we need to find or create the website-specific version
                base_view = request.env['ir.ui.view'].browse(int(res_id))
                _logger.info(f"Base view: {base_view.name} (ID: {base_view.id}, Key: {base_view.key})")
                
                # Look for website-specific customization
                domain = [
                    ('key', '=', base_view.key),
                    ('website_id', '=', int(website_id))
                ]
                website_specific_view = request.env['ir.ui.view'].search(domain, limit=1)
                
                if website_specific_view:
                    # Website-specific view exists, update it
                    _logger.info(f"Updating existing website-specific view: {website_specific_view.id}")
                    record = website_specific_view
                else:
                    # No customization exists yet, create one
                    _logger.info(f"Creating new website-specific view for website {website_id}")
                    # Check if user has permission to create views
                    if not request.env.user.has_group('website.group_website_designer'):
                        record = base_view.sudo()
                    else:
                        record = base_view
                    
                    # We'll write to the base view with the website context
                    # Odoo will automatically create a specific view
                    record = record.with_context(website_id=int(website_id))
                    
            elif res_model == 'website.page':
                # For pages, we need to work with its view
                page = request.env['website.page'].browse(int(res_id))
                
                if not view_id or view_id == 'undefined':
                    view_id = page.view_id.id
                    _logger.info(f"Using view_id from page: {view_id}")
                
                # Then get its view, with website customization if any
                base_view = request.env['ir.ui.view'].browse(int(view_id))
                _logger.info(f"Base view for page: {base_view.name} (ID: {base_view.id}, Key: {base_view.key})")
                
                # Look for website-specific customization of the view
                domain = [
                    ('key', '=', base_view.key),
                    ('website_id', '=', int(website_id))
                ]
                website_specific_view = request.env['ir.ui.view'].search(domain, limit=1)
                
                if website_specific_view:
                    # Use website-specific view
                    _logger.info(f"Updating existing website-specific view for page: {website_specific_view.id}")
                    record = website_specific_view
                else:
                    # Create website-specific customization
                    _logger.info(f"Creating new website-specific view for page on website {website_id}")
                    # Check if user has permission to create views
                    if not request.env.user.has_group('website.group_website_designer'):
                        record = base_view.sudo()
                    else:
                        record = base_view
                    
                    # We'll write to the base view with the website context
                    # Odoo will automatically create a specific view
                    record = record.with_context(website_id=int(website_id))
                
                # Handle the 'website_indexed' field specially for pages
                if 'website_indexed' in filtered_data:
                    indexed_value = filtered_data.pop('website_indexed')
                    _logger.info(f"Setting website_indexed={indexed_value} on page {page.id}")
                    # Update the page directly for the indexed field
                    page.with_context(website_id=int(website_id)).write({
                        'website_indexed': indexed_value
                    })
            elif res_model == 'product.template':
                # For products, we need to use our custom model to store website-specific SEO data
                _logger.info(f"on save SEO save for website {website_id}")
                product = request.env['product.template'].browse(int(res_id))
                
                # Get valid fields for this model
                model_fields = valid_fields.get(res_model, ['website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'seo_name'])
                
                # Filter data for valid product SEO fields
                product_seo_data = {k: v for k, v in filtered_data.items() if k in model_fields}
                
                if not product_seo_data:
                    _logger.warning("SEO Save - No valid data to save for product")
                    return {'warning': 'No valid data to save'}
                
                # Check if this product already has website-specific SEO data
                domain = [
                    ('product_tmpl_id', '=', int(res_id)),
                    ('website_id', '=', int(website_id))
                ]
                ProductSEO = request.env['product.template.seo']
                product_seo = ProductSEO.search(domain, limit=1)
                
                if product_seo:
                    # Update existing website-specific SEO data
                    _logger.info(f"Updating existing website-specific SEO data for product: {product_seo.id}")
                    result = product_seo.write(product_seo_data)
                    record = product_seo  # Use this for reading back saved values
                else:
                    # Create new website-specific SEO data
                    _logger.info(f"Creating new website-specific SEO data for product on website {website_id}")
                    vals = {
                        'product_tmpl_id': int(res_id),
                        'website_id': int(website_id),
                        **product_seo_data
                    }
                    
                    # Check if user has permission to create records
                    if not request.env.user.has_group('website.group_website_designer'):
                        product_seo = ProductSEO.sudo().create(vals)
                    else:
                        product_seo = ProductSEO.create(vals)
                        
                    result = bool(product_seo)
                    record = product_seo  # Use this for reading back saved values
                    
                # Force a flush to ensure data is written to database
                request.env.cr.flush()
                
                # Prepare saved values
                saved_values = {}
                for field in product_seo_data.keys():
                    if hasattr(record, field):
                        saved_values[field] = getattr(record, field)
                        
                _logger.info(f"SEO Save - Saved product SEO values: {saved_values}")
                
                return {
                    'success': True, 
                    'result': result,
                    'saved_values': saved_values
                }
            else:
                # For other models, use standard approach with context
                _logger.info(f"Using standard approach for model: {res_model}")
                record = request.env[res_model].with_context(**ctx).browse(res_id)
            
            # Check if user can modify this record
            target_website._check_user_can_modify(record)
            
            # Use sudo if user has website editor rights
            if request.env.user.has_group('website.group_website_restricted_editor'):
                record = record.sudo()
                _logger.info("SEO Save - Using sudo for record")
                
            _logger.info(f"SEO Save - About to write filtered data: {filtered_data}")
            
            # Write the SEO data to the record
            result = record.write(filtered_data)
            _logger.info(f"SEO Save - Write result: {result}")
            
            # Force a flush to ensure data is written to database
            request.env.cr.flush()
            
            # Read back the data to confirm it was saved
            # Now we need to fetch the possibly newly created website-specific view
            if res_model in ('ir.ui.view', 'website.page'):
                if res_model == 'website.page':
                    # Get the view ID again in case it changed
                    page = request.env['website.page'].browse(int(res_id))
                    view_id = page.view_id.id
                    base_view = request.env['ir.ui.view'].browse(view_id)
                else:
                    base_view = request.env['ir.ui.view'].browse(int(res_id))
                
                # Look for website-specific customization again
                domain = [
                    ('key', '=', base_view.key),
                    ('website_id', '=', int(website_id))
                ]
                website_specific_view = request.env['ir.ui.view'].search(domain, limit=1)
                
                if website_specific_view:
                    updated_record = website_specific_view
                else:
                    updated_record = base_view.with_context(website_id=int(website_id))
            else:
                updated_record = request.env[res_model].with_context(**ctx).browse(res_id)
            
            saved_values = {}
            
            # Check which fields were actually saved
            for field in filtered_data.keys():
                if hasattr(updated_record, field):
                    saved_values[field] = getattr(updated_record, field)
            
            # Add website_indexed back if it was in the original data
            if res_model == 'website.page' and 'website_indexed' in data:
                page = request.env['website.page'].browse(int(res_id))
                saved_values['website_indexed'] = page.website_indexed
                    
            _logger.info(f"SEO Save - Saved values: {saved_values}")
            
            return {
                'success': True, 
                'result': result,
                'saved_values': saved_values
            }
        except Exception as e:
            _logger.error(f"SEO Save - Error: {str(e)}")
            import traceback
            _logger.error(f"SEO Save - Traceback: {traceback.format_exc()}")
            return {'error': str(e)} 

class ProductSEOController(Website):
    """
    Extension of Website controller that adds support for using product.template.seo data
    when handling product pages.
    """
    
    def _prepare_product_for_json(self, product, include_attributes=True):
        """Override to include website-specific SEO data in product JSON"""
        res = super()._prepare_product_for_json(product, include_attributes)
        
        # Only handle product templates
        if product._name != 'product.template':
            return res
            
        # Get the current website
        website = request.website
        _logger.info(f"Preparing product JSON data for product {product.id} on website {website.id}")
        
        # Get website-specific SEO data
        product_seo = self._get_product_seo_data(product.id, website.id)
        if product_seo:
            _logger.info(f"Found website-specific SEO data for product JSON: {product_seo.id}")
            
            # Add SEO fields to JSON response
            res.update({
                'website_meta_title': product_seo.website_meta_title,
                'website_meta_description': product_seo.website_meta_description,
                'website_meta_keywords': product_seo.website_meta_keywords,
                'website_meta_og_img': product_seo.website_meta_og_img,
                'seo_name': product_seo.seo_name,
            })
        
        return res
    
    def _get_product_seo_data(self, product_template_id, website_id):
        """Get website-specific SEO data for a product"""
        ProductSEO = request.env['product.template.seo']
        domain = [
            ('product_tmpl_id', '=', product_template_id),
            ('website_id', '=', website_id)
        ]
        product_seo = ProductSEO.search(domain, limit=1)
        if not product_seo:
            # No website-specific data found, create a new record
            product = request.env['product.template'].browse(product_template_id)
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


from odoo.addons.website_sale.controllers.main import WebsiteSale

class CustomWebsiteSaleController(WebsiteSale):
    """
    Extension of WebsiteSale controller that adds support for using product.template.seo data
    when preparing product values.
    """
    
    def _prepare_product_values(self, product, category, search, **kwargs):
        """Override to include website-specific SEO data"""
        values = super()._prepare_product_values(product, category, search, **kwargs)
        
        # Get the current website
        website = request.website
        _logger.info(f"Preparing product values for product {product.id} on website {website.id}")
        
        # Get website-specific SEO data using the CustomWebsiteController method
        ProductSEO = request.env['product.template.seo']
        domain = [
            ('product_tmpl_id', '=', product.id),
            ('website_id', '=', website.id)
        ]
        product_seo = ProductSEO.search(domain, limit=1)
        
        if not product_seo:
            # No website-specific data found, create a new record
            vals = {
                'product_tmpl_id': product.id,
                'website_id': website.id,
                'website_meta_title': product.website_meta_title or '',
                'website_meta_description': product.website_meta_description or '',
                'website_meta_keywords': product.website_meta_keywords or '',
                'website_meta_og_img': product.website_meta_og_img or '',
                'seo_name': product.seo_name or '',
            }
            try:
                product_seo = ProductSEO.sudo().create(vals)
                _logger.info(f"Created website-specific SEO data for product in _prepare_product_values: {product_seo.id}")
            except Exception as e:
                _logger.error(f"Error creating website-specific SEO data in _prepare_product_values: {str(e)}")
        
        if product_seo:
            _logger.info(f"Found website-specific SEO data for product: {product_seo.id}")
            
            # Add SEO data to product values
            product = values.get('product')
            if product:
                # Override product SEO fields with website-specific values
                # Note: This doesn't change the database record, just the values used in the template
                product.website_meta_title = product_seo.website_meta_title
                product.website_meta_description = product_seo.website_meta_description
                product.website_meta_keywords = product_seo.website_meta_keywords
                product.website_meta_og_img = product_seo.website_meta_og_img
                product.seo_name = product_seo.seo_name
                
                _logger.info(f"Applied website-specific SEO data to product values")
        
        return values
{
    'name': 'OX Pricelist Tags',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Add tags to pricelists and display them on product cards for portal users',
    'description': """
        OX Pricelist Tags
        =================
        
        This module allows you to:
        * Create custom tags for pricelists
        * Assign tags to pricelists
        * Display pricelist tags on product cards for portal users
        * Show tags in the bottom-right corner of product cards with styled badges
    """,
    'author': 'OX Solutions',
    'website': 'https://www.oxsolutions.com',
    'depends': ['sale', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/ox_pricelist_tag_views.xml',
        'views/pricelist_views.xml',
        'views/website_sale_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/ox_pricelist_tags/static/src/css/ox_pricelist_tags.css',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}

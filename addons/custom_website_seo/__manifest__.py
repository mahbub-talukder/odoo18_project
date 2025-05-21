{
    'name': 'Website SEO Multi-Website Selector',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Allows editing SEO metadata for multiple websites at once',
    'description': """
        This module adds a website selector dropdown in the Optimize SEO page,
        allowing users to edit SEO metadata for all websites from a single interface.
    """,
    'author': 'NexelBD',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_website_seo/static/src/js/seo_website_selector.js',
        ],
        'web.assets_frontend': [],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
} 
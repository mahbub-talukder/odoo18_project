{
    'name': 'Unified Sales',
    'version': '1.0',
    'summary': 'Integration with external API and automated sales workflow',
    'description': """
        This module integrates with external API (e.g., Shopify) to create quotations
        and automates the sales process when payments are confirmed.
    """,
    'category': 'Sales',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale_management',
        'account',
        'payment',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/api_config_views.xml',
        'views/menu_views.xml',
        'views/unified_sales_workflow_process_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
} 
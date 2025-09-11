{
    'name': 'OX Commission Sales',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Manage sales commissions with automated tracking and vendor bills',
    'description': """
        Commission Sales Management System
        ===================================
        - 20% commission on first orders
        - 10% residual commission on repeat orders
        - Biweekly automated payouts
        - Commission plan management with approval workflow
        - Real-time commission tracking
        - Automated vendor bill generation
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale_management', 'account', 'mail'],
    'data': [
        'security/commission_security.xml',
        'security/ir.model.access.csv',
        'views/commission_plan_views.xml',
        'views/commission_tracking_views.xml',
        'views/menu_views.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'icon': '/ox_comission_sales/static/description/icon.png',
}
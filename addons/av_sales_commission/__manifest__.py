# -*- coding: utf-8 -*-
{
    'name': 'Sales Commission Management/Plans',
    'title': 'Sales Commission Management/Plans',
    'version': '18.0.1.1',
    'category': 'Sales',
    'summary': 'Custom commission plans for salespersons or sales teams',
    'author': 'OutsetX',
    'license': 'LGPL-3',
    'depends': ['sale_management', 'sales_team', 'hr', 'account'],
    'data': [
        'security/sales_commission_security.xml',
        'security/ir.model.access.csv',
        'security/sales_commission_rules.xml',
        'data/default_groups.xml',
        'views/sales_commission_views.xml',
        'views/sales_commission_line_views.xml',
        'views/sales_commission_report_views.xml',
        'views/sales_commission_realtime_views.xml',
        'views/sales_commission_realtime_detail_views.xml',
        'views/actions_and_crons.xml',
        'views/menuitems.xml',
        'views/account_move_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'av_sales_commission/static/src/css/sales_commission.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

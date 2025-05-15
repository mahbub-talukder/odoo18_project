# -*- coding: utf-8 -*-
{
    'name': "Custom Shopify EPT Connector",

    'summary': "Customize Shopify connector's automation workflow",

    'description': """
Customizations for Shopify Connector module to implement the following:

- Customize the Shopify connector's automation workflow behavior
- Remove hard dependencies between automation steps: validate_order, create_invoice, and register_payment
- Allow payment creation without invoice generation
- Auto-reconcile payments with invoices when they are created
- Apply the same workflow logic to manual quotations created in Odoo
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale', 'account', 'common_connector_library', 'shopify_ept'],

    # always loaded
    'data': [
        'views/inherit_sales_workflow_process.xml',
        'views/inherit_sale_order.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}


# -*- coding: utf-8 -*-
{
    'name': "test_conciliation",

    'summary': """
        Prueba Técnica - Desarrollo Python/Odoo
        """,

    'description': """
        Prueba Técnica - Desarrollo Python/Odoo
    """,

    'author': "Levi",
    'website': "https://github.com/Levi2794/prueba_xepelin",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'wizard/import_excel_view.xml',
        'views/master_views.xml',
        'views/complemento_views.xml',
    ],
    'application': True,
    'installable': True,
}
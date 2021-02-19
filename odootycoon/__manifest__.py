# -*- coding: utf-8 -*-
{
    'name': "odootycoon",

    'summary': """
        Create a fun Business Tycoon Game Using Odoo's Framework""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Greg Moss",
    'website': "http://www.odooclass.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
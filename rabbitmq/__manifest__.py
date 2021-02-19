# -*- coding: utf-8 -*-
{
    'name': "rabbitmq",

    'summary': """
        RabbitMQ Fast/Easy Distributed Processing""",

    'description': """
        1. Break long processes down into manageable queues
        2. Create a centralized messaging architecture for complex systems
        3. Document your API's through a standard non-propriatary messaging system
        4. Provide better auditing
        5. Ability to implement additional controls and logging
    """,

    'author': "Greg Moss",
    'website': "http://www.odooclass.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

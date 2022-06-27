
# -*- coding: utf-8 -*-
{
    'name': 'Segments',
    'version': '1.0',
    'category': 'Sales/CRM',
    'author' : "Richard Németh",
    'description': """This module is extension for contacts. You are able to choose in which segment does your contact work.""",
        'summary': 'Centralize your address book with working segments',
    'depends': ['base'],
    'data': [
        'views/views.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
        ],
    'demo' : ['demo/demo_data.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

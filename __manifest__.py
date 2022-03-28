# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'JobSite',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'A pool of new opportunities',
    'sequence': -100,
    'description': """
        It is an entity of location type which generates new leads.
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/jobsite_list.xml',
        'views/jobsite.xml'
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
}

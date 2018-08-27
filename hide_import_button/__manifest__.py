# -*- coding: utf-8 -*-
{
    'name': 'Show Import Button - Based on User Groups',
    'version': '10.0.1.2',
    'license': 'LGPL-3',
    'category': 'Tools',
    "sequence": 1,
    'summary': 'This module is used for restrict the import button for user level access.',
    'complexity': "easy",
    'description': """
        This module hide the 'Import' button by default.
        If you want to show 'Import' button for a specific user you have to select 'Show Import Button' group in user form.

    """,
    'author': 'Nivas M',
    'depends': ['base', 'web'],
    'data': ['security/security.xml',
             'views/webclient_templates.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

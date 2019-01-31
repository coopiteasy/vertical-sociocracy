# -*- coding: utf-8 -*-
#
#  Copyright (C) 2019  Coop IT Easy SCRLfs. <http://www.coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shared Governance Base",
    "version": "1.0",
    "depends": ['base',
                'mail',
                'document',
                ],
    "author": "Coop IT Easy SCRLfs",
    "category": "Cooperative management",
    "website": "www.coopiteasy.be",
    "license": "AGPL-3",
    "description": """

    """,
    'data': [
        'security/shared_governance_security.xml',
        # 'security/ir.model.access.csv',
        'views/shared_governance_menu.xml',
        'views/mandate.xml',
        'views/circle.xml',
        'views/policy.xml',
    ],
    'installable': True,
    'application': True,
}

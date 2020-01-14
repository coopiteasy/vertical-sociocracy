# -*- coding: utf-8 -*-
#
#  Copyright (C) 2019  Coop IT Easy SCRLfs. <http://www.coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shared Governance",
    "version": "1.0",
    "depends": ["base", "mail", "document"],
    "author": "Coop IT Easy SCRLfs",
    "category": "Cooperative Management",
    "website": "www.coopiteasy.be",
    "license": "AGPL-3",
    "description": """
        Shared Governance in Sociocracy organizations.
    """,
    "data": [
        "security/shared_governance_security.xml",
        "security/ir.model.access.csv",
        "views/mandate.xml",
        "views/res_partner.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
}

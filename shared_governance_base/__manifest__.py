#
#  Copyright (C) 2019  Coop IT Easy SC. <http://www.coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shared Governance",
    "version": "12.0.1.0.0",
    "depends": ["mail"],
    "author": "Coop IT Easy SC",
    "category": "Cooperative Management",
    "website": "https://github.com/coopiteasy/vertical-sociocracy",
    "license": "AGPL-3",
    "summary": """
        Shared Governance in Sociocracy organizations.
    """,
    "data": [
        "security/shared_governance_security.xml",
        "security/ir.model.access.csv",
        "views/mandate.xml",
        "views/res_partner.xml",
        "views/menus.xml",
    ],
    "application": True,
}

# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    sg_type = fields.Selection(
        string="Shared Governance Type",
        selection=[("person", "Person"), ("circle", "Circle")],
    )

    mandate_ids = fields.One2many(
        comodel_name="sg.mandate",
        inverse_name="partner_id",
        string="Mandates",
        read_only=True,
    )

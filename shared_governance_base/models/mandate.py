# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Mandate(models.Model):
    _name = "sg.mandate"

    _inherit = ["mail.thread", "ir.needaction_mixin"]

    name = fields.Char(string="Name", required=True)
    purpose = fields.Html(string="Purpose")
    partner_id = fields.Many2one(
        string="Assigned Person",
        comodel_name="res.partner",
        default=lambda self: self.env.user.partner_id,
        domain="[('sg_type', '!=', False)]",
        track_visibility="onchange",
    )
    state = fields.Selection(
        [("draft", "Draft"), ("alive", "Alive"), ("archived", "Archived")],
        string="State",
        default="alive",
        track_visibility="onchange",
    )

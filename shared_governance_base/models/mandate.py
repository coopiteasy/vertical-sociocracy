# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Mandate(models.Model):
    _name = "sg.mandate"

    _inherit = ["mail.thread", "ir.needaction_mixin"]

    name = fields.Char(string="Name", required=True)
    purpose = fields.Html(string="Purpose")
    user_id = fields.Many2one(
        string="Assigned Person",
        comodel_name="res.users",
        default=lambda self: self.env.user,
        track_visibility="onchange",
    )
    state = fields.Selection(
        [("draft", "Draft"), ("alive", "Alive"), ("archived", "Archived")],
        string="State",
        default="draft",
        track_visibility="onchange",
    )

    @api.multi
    def action_draft(self):
        self.write({"state": "draft"})

    @api.multi
    def action_alive(self):
        self.write({"state": "alive"})

    @api.multi
    def action_archive(self):
        self.write({"state": "archived"})

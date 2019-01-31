# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Mandate(models.Model):
    _name = 'shared.governance.mandate'

    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char(
        string='Name',
    )
    purpose = fields.Html(
        string='Purpose',
    )
    circle_id = fields.One2many(
        'shared.governance.circle',
        'mandate_id',
        string='Assigned Circle',
    )
    person_id = fields.Many2one(
        string='Assigned Person',
        comodel_name='res.users',
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('alive', 'Alive'),
         ('archived', 'Archived')],
        string='State',
        default='draft')
    # todo constraint: either circle or res_users

    @api.multi
    def action_alive(self):
        self.write({'state': 'alive'})

    @api.multi
    def action_archive(self):
        self.write({'state': 'archived'})

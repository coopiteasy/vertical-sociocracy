# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Policy(models.Model):
    _name = 'shared.governance.policy'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Name',
        required=True,
    )
    circles = fields.One2many(
        comodel_name='shared.governance.circle',
        inverse_name='policy_id',
        string='Circles',
    )
    policy = fields.Html(
        string='Policy',
    )
    attachment_ids = fields.One2many(
        'ir.attachment',
        'res_id',
        domain=[('res_model', '=', 'shared.governance.policy')],
        string='Attachments',
    )
    attachment_number = fields.Integer(
        compute='_get_attachment_number',
        string="Number of Attachments"
    )

    @api.multi
    def _get_attachment_number(self):
        read_group_res = self.env['ir.attachment'].read_group(
            [('res_model', '=', 'hr.applicant'), ('res_id', 'in', self.ids)],
            ['res_id'], ['res_id'])
        attach_data = dict((res['res_id'], res['res_id_count']) for res in read_group_res)
        for record in self:
            record.attachment_number = attach_data.get(record.id, 0)

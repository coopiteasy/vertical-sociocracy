# -*- coding: utf-8 -*-
from openerp import api, fields, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    email = fields.Char(
        related='partner_id.email')
    phone = fields.Char(
        related='partner_id.phone')
    lang = fields.Selection(
        related='partner_id.lang')

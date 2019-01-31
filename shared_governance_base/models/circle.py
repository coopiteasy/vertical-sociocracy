# -*- coding: utf-8 -*-
from openerp import api, fields, models, _

from openerp.exceptions import ValidationError


class Circle(models.Model):
    _name = 'shared.governance.circle'
    _constraints = [
        (models.Model._check_recursion,
         'Error ! You cannot create recursive'
         ' circle.',
         ['parent_id'])
    ]

    name = fields.Char(
        string='Name',
        required=True,
    )
    mandate_id = fields.Many2one(
        comodel_name='shared.governance.mandate',
        string='Mandate',
        domain=[('state', '=', 'alive')])
    state = fields.Selection(
        related='mandate_id.state',
        string='State')
    parent_id = fields.Many2one(
        comodel_name='shared.governance.circle',
        string='Parent circle',
        select=True)
    child_ids = fields.One2many(
        'shared.governance.circle',
        'parent_id',
        string='Childs Circle',
        domain=[('state', '=', 'alive')])
    members = fields.Many2many(
        comodel_name='res.users',
        string='Members')
    policy_id = fields.Many2one(
        comodel_name='shared.governance.policy',
        string='Policy',
    )

    @api.multi
    def unlink(self):
        for circle in self:
            if circle.members:
                raise ValidationError(_("You can't delete the circle named %s"
                                        " : You should first remove"
                                        " all members") % (circle.name))
            elif circle.child_ids:
                raise ValidationError(_("You can't delete the circle named %s"
                                        " : You should first delete the childs"
                                        " circle") % (circle.name))
            else:
                super(Circle, circle).unlink()

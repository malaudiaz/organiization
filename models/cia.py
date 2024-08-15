# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo import _

class cia(models.Model):
    _name = "res.company"
    _inherit = "res.company"
    
    is_organization = fields.Boolean()
    
    type = fields.Many2one(
        string="Tipo de Organización",
        comodel_name="organization.type",
        ondelete="set null",
        help="Introduzca el Tipo de organización"
    )
    
    members = fields.One2many(
        string="Miembros", 
        comodel_name="res.partner",
        inverse_name="organization"
    )

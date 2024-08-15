# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import _

class type(models.Model):
    _name = "organization.type"
    _description = "organization.type"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el Nombre del tipo de organización"
    )
    
    description = fields.Text(
        string="Descripción",
        readonly=False,
        required=False,
        help="Introduzca la Descripción"
    )
    
    organization_type = fields.One2many(
        string="Organización", comodel_name="res.company", inverse_name="type"
    )
    

# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import _


class position(models.Model):
    _name = "organization.position"
    _description = "Cargos dentro de la organización"

    name = fields.Char(
        string="Cargo", readonly=False, required=True, help="Nombre del País"
    )

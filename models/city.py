# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import _


class city(models.Model):
    _name = "organization.city"
    _description = "Ciudades"

    name = fields.Char(
        string="Ciudad", readonly=False, required=True, help="Nombre de la Ciudad"
    )

    initials = fields.Char(
        string="Siglas",
        readonly=False,
        required=False,
    )

    country_id = fields.Many2one(
        string="País", comodel_name="organization.country", required=True
    )

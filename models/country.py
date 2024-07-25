# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import _


class country(models.Model):
    _name = "organization.country"
    _description = "Paises"

    name = fields.Char(
        string="País", readonly=False, required=True, help="Nombre del País"
    )

    initials = fields.Char(
        string="Siglas",
        readonly=False,
        required=True,
        help="Introduzca las siglas del País",
    )

    flag = fields.Binary(string="Bandera")

    city_id = fields.One2many(
        "organization.city",
        string="Ciudad",
        domain="[('country_id', '=', country_id)]",
        inverse_name="country_id",
        required=True,
    )

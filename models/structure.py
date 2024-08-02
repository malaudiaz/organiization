# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import _


class structure(models.Model):
    _name = "organization.structure"
    _description = "Estructura de la organizacion"

    organization = fields.Many2one(
        comodel_name="organization.organization", string="Organización"
    )

    position = fields.Many2one(comodel_name="organization.position", string="Cargo")

    member = fields.Many2one(string="Miembro", comodel_name="organization.members", ondelete="set null")

    _sql_constraints = [
        (
            "unique_position",
            "unique(organization, position)",
            "Los cargos son únicos por organización",
        ),
        (
            "unique_member",
            "unique(organization, member)",
            "Miembro repetido",
        ),
    ]

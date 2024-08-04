# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import _


class structure(models.Model):
    _name = "organization.structure"
    _description = "Estructura de la organizacion"

    organization = fields.Many2one(
        comodel_name="organization.organization", string="Organización"
    )

    position = fields.Many2one(comodel_name="organization.position", string="Cargo")
           
    members = fields.Many2one(
        string="Miembro",
        comodel_name="organization.members",
        ondelete="set null"
    )

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
    
    @api.onchange("position")
    def _onchange_position(self):
        members = self._get_members()
        self.members = [(4, members.id)]  

    def _get_members(self):
        for member in self:
            members = member.env["organization.organization"].search([("organization_id", "=", "1")])
            if len(members) > 0:
                print("dfsdfdsf")
            else:
                print("dfsdfdsf")
            
            return members


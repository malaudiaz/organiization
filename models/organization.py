# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import _


class organization(models.Model):
    _name = "organization.organization"
    _description = "organizaciones definidas por tipo"
    # _inherit = "res.company"

    name = fields.Char(
        string="Nombre",
        readonly=False,
        required=True,
        help="Introduzca el Nombre del tipo de organización",
    )

    initials = fields.Char(
        string="Siglas",
        readonly=False,
        required=True,
        help="Introduzca las siglas de la organización",
    )

    logo = fields.Binary(string="Logotipo")
    file_name = fields.Char()

    type = fields.Many2one(
        string="Tipo de Organización",
        comodel_name="organization.type",
        store=True,
        help="Introduzca el Tipo de organización",
    )

    parent_id = fields.Many2one(
        string="Subordinada a", comodel_name="organization.organization"
    )

    child_ids = fields.One2many(
        string="Organización Subordinada",
        comodel_name="organization.organization",
        inverse_name="parent_id",
    )

    country_id = fields.Many2one(
        string="País",
        comodel_name="organization.country"
    )

    city_id = fields.Many2one(
        string="Ciudad",
        comodel_name="organization.city"
    )
       
    @api.onchange('country_id')
    def change_country_id(self):
        if self.country_id:
            domain = [('country_id', '=', self.country_id.id)]
        else:
            domain = []
        
        return {'domain': {'city_id': domain}}
       
    members = fields.Many2many(
        string="Miembros", 
        comodel_name="organization.members",
        relation="organization_member",
        column1="organization_id",
        column2="member_id"
    )
  
    structure = fields.One2many(
        string="Estructura", comodel_name="organization.structure", inverse_name="organization"
    )
    
# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import _

class members(models.Model):
    _name = "organization.members"
    _description = "miembros de las distintas organizacions"
    # _inherit = "res.company"
    
    firts_name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Nombre"
    )
    
    last_name = fields.Char(
        string="Apellidos", readonly=False, required=True, help="Apellidos"
    )
    
    photo = fields.Binary(string="Foto")

    alias = fields.Char(
        string="Alias", readonly=False, required=False, help="Alias"
    )

    phone = fields.Char(
        string="Teléfono", readonly=False, required=True, help="Teléfono"
    )

    email = fields.Char(
        string="Correo", readonly=False, required=False, help="Correo"
    )
    
    # def _get_default_org(self):
    #     org = self.browse(self._context.get("current_organization"))
    #     if org:
    #         return [org.id]
    #     else:
    #         return []    
    
    organization = fields.Many2many(
        string="Organización", 
        comodel_name="organization.organization", 
        relation="organization_member",        
        column1="organization_id",
        column2="member_id",   
        required=True     
    )

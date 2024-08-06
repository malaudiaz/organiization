# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import _


class structure(models.Model):
    _name = "organization.structure"
    _description = "Estructura de la organizacion"

    organization = fields.Many2one(
        comodel_name="organization.organization", string="Organización"
    )  
    
    # @api.onchange('organization')  # depends on the fields that make up your name
    # def _compute_organization_id(self):
    #     for record in self:         
    #         lines = []
    #         for i in record.organization.members:
    #             vals = (0,0,i)   
    #             lines.append((vals))
    #         record.members = lines
                             
            
    position = fields.Many2one(comodel_name="organization.position", string="Cargo")

    members = fields.Many2one(
        string="Miembro", 
        comodel_name="organization.members", 
        ondelete="set null",
        # domain="[('organization_id', '=', organization_id)]",
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

    display_member_id =  fields.Integer(compute='_compute_display_value')
    display_member_name = fields.Char(compute='_compute_display_value')

    @api.depends('organization')  # depends on the fields that make up your name
    def _compute_display_value(self):
        for record in self:          
            names = [record.members.firts_name, record.members.last_name]  # adjust this line based on your needs
            record.display_member_id = record.members.id
            record.display_member_name = ' '.join(filter(None, names))


    def _get_organization_members(self):
        for record in self:
            miembros = None            
            for item in record.organization.members:
                print(item.firts_name)
                miembros = item
            
            record.members = miembros



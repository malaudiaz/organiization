# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import _

class members(models.Model):
    _name = "organization.members"
    _description = "miembros de las distintas organizacions"
    # _inherit = "res.company"
    # _rec_name = "firts_name"
    
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
        string="Correo", readonly=False, required=True, help="Correo"
    )

    country_id = fields.Many2one(
        string="País",
        comodel_name="organization.country"
    )
           
    display_name = fields.Char(compute='_compute_display_name')

    @api.depends('firts_name', 'last_name')  # depends on the fields that make up your name
    def _compute_display_name(self):

        for record in self:

            names = [record.firts_name, record.last_name]  # adjust this line based on your needs

            record.display_name = ' '.join(filter(None, names))


# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo import _

class contacts(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    is_org_contact = fields.Boolean()
    
    organization = fields.Many2one(comodel_name="res.company", string="Organización", ondelete="cascade")

# -*- coding: utf-8 -*-
# from odoo import http


# class Organization(http.Controller):
#     @http.route('/organization/organization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/organization/organization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('organization.listing', {
#             'root': '/organization/organization',
#             'objects': http.request.env['organization.organization'].search([]),
#         })

#     @http.route('/organization/organization/objects/<model("organization.organization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('organization.object', {
#             'object': obj
#         })


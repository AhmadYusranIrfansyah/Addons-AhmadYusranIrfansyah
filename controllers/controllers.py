# -*- coding: utf-8 -*-
# from odoo import http


# class OctoStudio(http.Controller):
#     @http.route('/octo_studio/octo_studio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/octo_studio/octo_studio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('octo_studio.listing', {
#             'root': '/octo_studio/octo_studio',
#             'objects': http.request.env['octo_studio.octo_studio'].search([]),
#         })

#     @http.route('/octo_studio/octo_studio/objects/<model("octo_studio.octo_studio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('octo_studio.object', {
#             'object': obj
#         })

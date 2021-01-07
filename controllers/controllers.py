# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatLibrary(http.Controller):
#     @http.route('/viseducat_library/viseducat_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_library/viseducat_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_library.listing', {
#             'root': '/viseducat_library/viseducat_library',
#             'objects': http.request.env['viseducat_library.viseducat_library'].search([]),
#         })

#     @http.route('/viseducat_library/viseducat_library/objects/<model("viseducat_library.viseducat_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_library.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
from openerp import http

# class Ideastore(http.Controller):
#     @http.route('/ideastore/ideastore/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ideastore/ideastore/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ideastore.listing', {
#             'root': '/ideastore/ideastore',
#             'objects': http.request.env['ideastore.ideastore'].search([]),
#         })

#     @http.route('/ideastore/ideastore/objects/<model("ideastore.ideastore"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ideastore.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

# class Guo1(http.Controller):
#     @http.route('/guo1/guo1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/guo1/guo1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('guo1.listing', {
#             'root': '/guo1/guo1',
#             'objects': http.request.env['guo1.guo1'].search([]),
#         })

#     @http.route('/guo1/guo1/objects/<model("guo1.guo1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('guo1.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

# class Odootycoon(http.Controller):
#     @http.route('/odootycoon/odootycoon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odootycoon/odootycoon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odootycoon.listing', {
#             'root': '/odootycoon/odootycoon',
#             'objects': http.request.env['odootycoon.odootycoon'].search([]),
#         })

#     @http.route('/odootycoon/odootycoon/objects/<model("odootycoon.odootycoon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odootycoon.object', {
#             'object': obj
#         })
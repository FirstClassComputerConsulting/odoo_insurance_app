# -*- coding: utf-8 -*-
# from odoo import http


# class Rabbitmq(http.Controller):
#     @http.route('/rabbitmq/rabbitmq/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rabbitmq/rabbitmq/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rabbitmq.listing', {
#             'root': '/rabbitmq/rabbitmq',
#             'objects': http.request.env['rabbitmq.rabbitmq'].search([]),
#         })

#     @http.route('/rabbitmq/rabbitmq/objects/<model("rabbitmq.rabbitmq"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rabbitmq.object', {
#             'object': obj
#         })

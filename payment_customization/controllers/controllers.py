# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentCustomization(http.Controller):
#     @http.route('/payment_customization/payment_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_customization/payment_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_customization.listing', {
#             'root': '/payment_customization/payment_customization',
#             'objects': http.request.env['payment_customization.payment_customization'].search([]),
#         })

#     @http.route('/payment_customization/payment_customization/objects/<model("payment_customization.payment_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_customization.object', {
#             'object': obj
#         })

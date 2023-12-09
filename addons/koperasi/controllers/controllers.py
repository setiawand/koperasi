# -*- coding: utf-8 -*-
# from odoo import http


# class Koperasi(http.Controller):
#     @http.route('/koperasi/koperasi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/koperasi/koperasi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('koperasi.listing', {
#             'root': '/koperasi/koperasi',
#             'objects': http.request.env['koperasi.koperasi'].search([]),
#         })

#     @http.route('/koperasi/koperasi/objects/<model("koperasi.koperasi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('koperasi.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class HelpdeskCustom(http.Controller):
#     @http.route('/helpdesk_custom/helpdesk_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_custom/helpdesk_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_custom.listing', {
#             'root': '/helpdesk_custom/helpdesk_custom',
#             'objects': http.request.env['helpdesk_custom.helpdesk_custom'].search([]),
#         })

#     @http.route('/helpdesk_custom/helpdesk_custom/objects/<model("helpdesk_custom.helpdesk_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_custom.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class HrPayslipChangeState(http.Controller):
#     @http.route('/hr_payslip_change_state/hr_payslip_change_state/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payslip_change_state/hr_payslip_change_state/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payslip_change_state.listing', {
#             'root': '/hr_payslip_change_state/hr_payslip_change_state',
#             'objects': http.request.env['hr_payslip_change_state.hr_payslip_change_state'].search([]),
#         })

#     @http.route('/hr_payslip_change_state/hr_payslip_change_state/objects/<model("hr_payslip_change_state.hr_payslip_change_state"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payslip_change_state.object', {
#             'object': obj
#         })

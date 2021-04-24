# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval as eval


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    refunded_id = fields.Many2one(
        'hr.payslip',
        string='Refunded Payslip',
        readonly=True
    )

    def refund_sheet(self):
        res = super(HrPayslip, self).refund_sheet()
        self.write({'refunded_id': eval(res['domain'])[0][2][0] or False})
        return res

    def action_payslip_cancel(self):
        for payslip in self:
            if payslip.refunded_id and payslip.refunded_id.state != 'cancel':
                raise ValidationError(_("""To cancel the Original Payslip the
                    Refunded Payslip needs to be canceled first!"""))

            # moves = payslip.mapped('move_id')
            # if moves.filtered(lambda x: x.state == 'posted'):
            #     moves.filtered(lambda x: x.state == 'posted').button_cancel()
            #     moves.unlink()
            if payslip.move_id.journal_id.update_posted:
                payslip.move_id.button_cancel()
                payslip.move_id.unlink()
            else:
                payslip.move_id._reverse_moves()
                payslip.move_id.ref = _('Reversal of: %s') % (payslip.name) if payslip.name else _('Reversal of: %s') % (
                    payslip.move_id.name),

                payslip.move_id = False
        return self.write({'state': 'cancel'})

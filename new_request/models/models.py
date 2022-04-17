from odoo import api, fields, models


class NewRequest(models.Model):
    _inherit = "hr.applicant"

    button_sh = fields.Boolean(related='stage_id.button_show')

    def action_new_request(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Request',
            'res_model': 'approval.request',
            'view_mode': 'form',
            'view_id': self.env.ref('approvals.approval_request_view_form').id,
        }

    # @api.depends('stage_id')
    # def _compute_button_show(self):
    #     for rec in self:
    #             rec.button_show = True

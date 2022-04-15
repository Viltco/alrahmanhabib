from odoo import api, fields, models


class NewRequest(models.Model):
    _inherit = "hr.applicant"

    button_show = fields.Boolean(default=False, compute='_compute_button_show', store=True)

    def action_new_request(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Request',
            'res_model': 'approval.request',
            'view_mode': 'form',
            # 'domain': domain,
        }

    @api.depends('stage_id')
    def _compute_button_show(self):
        for rec in self:
            if rec.stage_id.name == "Contract Proposal":
                rec.button_show = True

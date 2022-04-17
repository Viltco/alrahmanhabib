from odoo import api, fields, models


class NewRequest(models.Model):
    _inherit = "hr.recruitment.stage"

    button_show = fields.Boolean(default=False, store=True, string='New Contract  Request')

    # @api.depends('stage_id')
    # def _compute_button_show(self):
    #     for rec in self:
    #             rec.button_show = True

from odoo import api, fields, models, _


class NewRequest(models.Model):
    _inherit = "hr.applicant"

    button_sh = fields.Boolean(related='stage_id.button_show')

    approval_request_count = fields.Integer(string='Request to Approve', compute='get_request_count')

    def action_new_request(self):
        print(self.name)
        try:
            form_view_id = self.env.ref("approvals.approval_request_view_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Request',
            'res_model': 'approval.request',
            'view_type': 'form',
            'view_mode': 'form',
            'context': {'default_category_id': 4,
                        'default_source': self.name},
            'domain':('category_id', '=', 4),
            'views': [(form_view_id, 'form')],
            'target': 'current',
        }

    def action_contract_approval(self):
        print('yes')
        return {
            'name': _('Requests'),
            'domain': [('category_id', '=', 4), ('source', '=', self.name)],
            'view_type': 'form',
            'res_model': 'approval.request',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_request_count(self):
        for rec in self:
            count = self.env['approval.request'].search_count([('category_id', '=', 4) , ('source', '=', self.name)])
            rec.approval_request_count = count
    # @api.depends('stage_id')
    # def _compute_button_show(self):
    #     for rec in self:
    #             rec.button_show = True


class ApprovalCategory(models.Model):
    _inherit = 'approval.request'

    source = fields.Char('Source', readonly=True)

from odoo import models, fields, api, _


class AccountMoveInh(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('review', 'Review'),
        ('approve', 'Approve'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')

    def action_post(self):
        self.state = 'review'

    def action_review(self):
        self.state = 'approve'

    def action_approve(self):
        return super(AccountMoveInh, self).action_post()

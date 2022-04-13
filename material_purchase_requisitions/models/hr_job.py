from odoo import models, fields


class HrJob(models.Model):
    _inherit = 'hr.job'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('recruit', 'Recruitment in Progress'),
        ('open', 'Not Recruiting')
    ], string='Status', readonly=True, required=True, tracking=True, copy=False, default='draft', help="Set whether the recruitment process is open or closed for this job position.")
    test = fields.Char('test')

    def set_draft(self):
        for rec in self:
            rec.state = 'draft'
        print('Draft.......................................')

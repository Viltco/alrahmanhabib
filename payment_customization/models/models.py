# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError,ValidationError
from lxml import etree

class PaymentCustomization(models.Model):
    _inherit = 'account.payment'

    destination_account_id = fields.Many2one(
        comodel_name='account.account',
        string='Destination Account',
        store=True, readonly=False,
        compute='_compute_destination_account_id',
        domain="[('user_type_id.type', 'in', ('receivable', 'payable', 'liquidity')), ('company_id', '=', company_id)]",
        check_company=True)

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('review', 'Reviewed'),
        ('approve', 'Approved'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')

    def action_post(self):
        self.write({
            'state': 'confirm'
        })

    def action_review(self):
        self.write({
            'state': 'review'
        })

    def action_approve(self):
        rec = super(PaymentCustomization, self).action_post()
        self.write({
            'state': 'approve'
        })
        return rec

    def action_print_approve(self):
        self.write({
            'state': 'posted'
        })

    def action_draft(self):
        self.write({
            'state': 'draft'
        })
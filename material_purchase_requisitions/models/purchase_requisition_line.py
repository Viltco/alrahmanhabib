# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaterialPurchaseRequisitionLine(models.Model):
    _name = "material.purchase.requisition.line"
    _description = 'Material Purchase Requisition Lines'

    requisition_id = fields.Many2one(
        'material.purchase.requisition',
        string='Requisitions',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
    )
    #     layout_category_id = fields.Many2one(
    #         'sale.layout_category',
    #         string='Section',
    #     )
    description = fields.Char(
        string='Description',
        required=True,
    )
    qty = fields.Float(
        string='Quantity',
        default=1,
        required=True,
    )
    uom = fields.Many2one(
        'uom.uom',  # product.uom in odoo11
        string='Unit of Measure',
        required=True,
    )
    partner_id = fields.Many2many(
        'res.partner',
        string='Vendors',
    )

    requisition_type = fields.Selection(
        selection=[
            ('internal', 'Internal Picking'),
            ('purchase', 'Purchase Order'),
            ('recruitment', 'Recruitment'),
        ],
        string='Requisition Action',
        default='purchase',
        required=True,
    )
    job_positions = fields.Many2one('hr.job', 'Job Positions')
    job_description = fields.Text('Job Description', related='job_positions.description', readonly=False)
    no_of_recruit = fields.Integer('Excepted New Employees', related='job_positions.no_of_recruitment', readonly=False)

    @api.onchange('product_id')
    def onchange_product_id(self):
        for rec in self:
            rec.description = rec.product_id.name
            rec.uom = rec.product_id.uom_id.id


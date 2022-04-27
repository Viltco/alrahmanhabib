# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
import csv
from datetime import datetime
from datetime import date
import xlrd
import base64


class ProjectsXLSX(models.Model):
    _inherit = 'project.project'

    # file_upload = fields.Binary(string='Upload File')

    def create_data(self):
        wb = xlrd.open_workbook(file_contents=base64.decodestring(self.file_upload))
        for s in wb.sheets():
            first_row = []  # Header
            for col in range(s.ncols):
                first_row.append(s.cell_value(0, col))
            data = []
            for row in range(1, s.nrows):
                elm = {}
                for col in range(s.ncols):
                    elm[first_row[col]] = s.cell_value(row, col)
                data.append(elm)

        for i in data:
            line_val = []
            # partner_records = self.env['res.partner'].search([('name', '=', i.get('Contact'))], limit=1)
            # product_records = self.env['product.template'].search([('name', '=', i.get('Operations / Product'))], limit=1)
            # branch_records = self.env['res.branch'].search([('name', '=', i.get('Branch'))], limit=1)
            # uom_records = self.env['uom.uom'].search([('name', '=', i.get('Operations / Unit Of Measure'))], limit=1)
            # operation_records = self.env['stock.picking.type'].search([('name', '=', i.get('Operation Type'))],limit=1)
            # location_records = self.env['stock.location'].search([('complete_name', '=', i.get('Operations / From'))])
            # location_dest_records = self.env['stock.location'].search([('complete_name', '=', i.get('Operations / To'))])
            user_records = self.env['res.users'].search([('name', '=', i.get('resource_list'))])

            # if i.get('Contact') != '':
            # line_val.append((0, 0, {
            #     'product_id': product_records.product_variant_id.id,
            #     'name': product_records.product_variant_id.name,
            #     'product_uom': uom_records.id,
            #     'location_id': location_records.id,
            #     'location_dest_id': location_dest_records.id,
            #     'quantity_done': i.get('Operations / Done'),
            # }))
            start_tin = False
            end_tin = False
            if i.get('start_date'):
                start_seconds = (i.get('start_date') - 25569) * 86400.0
                start_tin = datetime.utcfromtimestamp(start_seconds)
            if i.get('end_date'):
                end_seconds = (i.get('end_date') - 25569) * 86400.0
                end_tin = datetime.utcfromtimestamp(end_seconds)
            # date_from = datetime.strptime(i.get('start_date'))
            # print(date_from)
            vals = {
                'name': i.get('task_name'),
                'task_code': i.get('task_code'),
                'date_start': start_tin,
                'date_deadline': end_tin,
                'user_id': user_records.id,
                'project_id': self.id,
                'company_id': self.env.company.id,
            }
            record = self.env['project.task'].create(vals)


class ProjectTaskXLSX(models.Model):
    _inherit = 'project.task'

    date_start = fields.Date(string='Start Date')
    task_code = fields.Char(string='Task Code')



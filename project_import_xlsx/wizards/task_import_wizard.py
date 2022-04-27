# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning
from datetime import datetime
from datetime import date
import xlrd
import base64


class TaskImport(models.TransientModel):
    _name = "task.import.wizard"
    _description = "Task Import Wizard"

    file_upload = fields.Binary(string='Upload File')

    def create_data(self):
        model = self.env.context.get('active_model')
        rec_model = self.env[model].browse(self.env.context.get('active_id'))
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
            user_records = self.env['res.users'].search([('name', '=', i.get('resource_list'))])
            start_tin = False
            end_tin = False
            if i.get('start_date'):
                start_seconds = (i.get('start_date') - 25569) * 86400.0
                start_tin = datetime.utcfromtimestamp(start_seconds)
            if i.get('end_date'):
                end_seconds = (i.get('end_date') - 25569) * 86400.0
                end_tin = datetime.utcfromtimestamp(end_seconds)
            vals = {
                'name': i.get('task_name'),
                'task_code': i.get('task_code'),
                'date_start': start_tin,
                'date_deadline': end_tin,
                'user_id': user_records.id,
                # 'project_id': self.id,
                'project_id': rec_model.id,
                # 'company_id': self.env.company.id,
            }
            record = self.env['project.task'].create(vals)

from odoo import models


class ReportXlsx(models.AbstractModel):
    _name = 'report.bolivia_payroll.report_id_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, report):
        sheet = workbook.add_worksheet('Bolivia Payroll')
        center = workbook.add_format({'align': 'center'})
        style = workbook.add_format({'bold': True, 'align': 'center'})
        date_style = workbook.add_format(
            {'text_wrap': True, 'num_format': 'dd-mm-yyyy', 'align': 'center', 'font_size': 8})

        sheet.set_column('D:M', 18)
        sheet.set_column('N:Z', 28)

        employee = self.env['hr.contract'].search([])
        row = 11
        col = 3
        for obj in report:
            sheet.write(row, col, 'SR #', style)
            col += 1
            sheet.write(row, col, 'ID Number', style)
            col += 1
            sheet.write(row, col, 'Ext.', style)
            col += 1
            sheet.write(row, col, 'Name and last name', style)
            col += 1
            sheet.write(row, col, 'Nationality', style)
            col += 1
            sheet.write(row, col, 'Birthday', style)
            col += 1
            sheet.write(row, col, 'Sex', style)
            col += 1
            sheet.write(row, col, 'Job Title', style)
            col += 1
            sheet.write(row, col, 'Date Of Joining', style)
            col += 1
            sheet.write(row, col, 'Paid Hours', style)
            col += 1
            sheet.write(row, col, 'Paid Days', style)
            col += 1
            sheet.write(row, col, 'Salary(Haber básico)', style)
            col += 1
            sheet.write(row, col, 'Pension(Bono de Antigüedad)', style)
            col += 1
            sheet.write(row, col, 'Production Bonus(Bono de producción)', style)
            col += 1
            sheet.write(row, col, 'Border(Subsidio de frontera)', style)
            col += 1
            sheet.write(row, col, 'Normal+Saturday(Trabajo extraordi-nario y nocturno)', style)
            col += 1
            sheet.write(row, col, 'Sunday(Pago dominical y domingo trabajado)', style)
            col += 1
            sheet.write(row, col, 'Other payment(Otros pagos)', style)
            col += 1
            sheet.write(row, col, 'Total( TOTAL GANADO)', style)
            col += 1
            sheet.write(row, col, 'jubilado - yes or no(Aporte a las AFPs)', style)
            col += 1
            sheet.write(row, col, 'Taxes(RC-IVA)', style)
            col += 1
            sheet.write(row, col, 'Other Discounts(Otros descuentos)', style)
            col += 1
            sheet.write(row, col, 'TOTAL DESCUENTOS', style)
            col += 1
            sheet.write(row, col, 'LÍQUIDO PAGABLE', style)

        sr_no = 0
        for e in employee:
            row += 1
            sr_no = sr_no + 1
            sheet.write(row, 3, sr_no, center)
            sheet.write(row, 4, e.employee_id.number, center)
            sheet.write(row, 5, e.employee_id.number, center)
            sheet.write(row, 6, e.employee_id.name, center)
            sheet.write(row, 7, e.employee_id.country_id.name, center)
            sheet.write(row, 8, e.employee_id.birthday, date_style)
            sheet.write(row, 9, e.employee_id.gender, center)
            sheet.write(row, 10, e.employee_id.job_id.name, center)
            sheet.write(row, 11, e.date_start, date_style)
            sheet.write(row, 12, e.employee_id.paid_hours, center)
            sheet.write(row, 13, e.employee_id.paid_days, center)
            sheet.write(row, 13, e.wage, center)
            sheet.write(row, 14, e.employee_id.pension, center)
            sheet.write(row, 15, e.employee_id.production_bonus, center)
            sheet.write(row, 16, e.employee_id.border, center)
            sheet.write(row, 17, e.employee_id.normal_saturday, center)
            sheet.write(row, 18, e.employee_id.sunday, center)
            sheet.write(row, 19, e.employee_id.other_payment, center)
            sheet.write(row, 20, e.employee_id.yes_or_no, center)
            sheet.write(row, 21, e.employee_id.taxes, center)
            sheet.write(row, 22, e.employee_id.other_discounts, center)


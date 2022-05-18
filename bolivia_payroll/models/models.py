from odoo import models, fields, api
from datetime import datetime
from pytz import timezone



class bolivia_payroll(models.Model):
    _inherit = 'hr.employee'

    pension = fields.Float("Pension(Bono de Antigüedad)")
    production_bonus = fields.Float("Production Bonus(Bono de producción)")
    border = fields.Float("Border(Subsidio de frontera)")
    normal_saturday = fields.Float("Normal + Saturday(Trabajo extraordi-nario y nocturno)")
    sunday = fields.Float("Sunday(Pago dominical y domingo trabajado)")
    other_payment = fields.Float("Other Payment(Otros pagos)")

    yes_or_no = fields.Float("jubilado - yes or no")
    taxes = fields.Float("Taxes(RC-IVA)")
    other_discounts = fields.Float("Other Discounts(Otros descuentos)")

    number = fields.Integer("ID Number")
    paid_hours = fields.Integer("ID Number"  , default=8 , readonly="True")
    paid_days = fields.Integer("ID Number" , default=30 , readonly="True")

# class EmployeeID(models.Model):
#     _inherit = 'hr.employee'
#

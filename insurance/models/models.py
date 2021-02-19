# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class insurance_policy(models.Model):
    _name = 'insurance.policy'
    _description = 'Insurance Policy'

    name = fields.Char()
    responsible_id = fields.Many2one('hr.employee')
    plan_duration = fields.Selection('insurance.plan_type',related="plan_type_id.plan_duration") 
    plan_type_id = fields.Many2one('insurance.plan_type')
    notes = fields.Text()
    
class insurance_plan_type(models.Model):
    _name = 'insurance.plan_type'
    _description = 'Insurance Plan Type'
    name = fields.Char()
    plan_duration= fields.Selection([('month', 'Monthly'), ('year', 'Yearly')])
    responsible_id = fields.Many2one('hr.employee')
    notes = fields.Text()


class insurance_employeepolicy(models.Model):
    _name = 'insurance.employeepolicy'
    _description = 'Employee Policies'
    employee_id = fields.Many2one('hr.employee')
    provider_id = fields.Many2one('res.partner')
    provider_notes = fields.Text("Provider Notes")
    policy_id = fields.Many2one('insurance.policy')
    deduction_amt = fields.Float("Deduction Amt")
    copay_amt = fields.Float("CoPay Amt")
    policy_responsible = fields.Many2one('hr.employee',related="policy_id.responsible_id") 
    effective_date = fields.Date()
    plan_terminated = fields.Boolean("Plan terminated",readonly=True)
    plan_terminated_date = fields.Date("Plan Terminated On",readonly=True)
    plan_review_required = fields.Boolean('Plan Review Required')
    plan_review_date = fields.Date('Plan Review Date')
    notes = fields.Text()

    def action_terminate_policy(self):
        print("Terminate Policy")
        for record in self:
            record.plan_terminated = True
            record.plan_terminated_date = fields.Date.today()
        
        # Return an action to fire it off
        #action = self.env.ref('insurance.policy_action_window').read()[0]
        #return action

    def action_reinstate_policy(self):
        print("Reinstate Policy")
        for record in self:
            record.plan_terminated = False
            record.plan_terminated_date = None

        
class insurance_employee(models.Model):
    _inherit = 'hr.employee'

    insurance_plans = fields.One2many('insurance.employeepolicy','employee_id')
    age = fields.Float(compute="_compute_age", store=True)
    EligibilityNotes_401k = fields.Text("Notes on 401k Elgibility")
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = (fields.Date.today() - record.birthday) / timedelta(days=365.2425)
            else:
                record.age = 0.0




#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

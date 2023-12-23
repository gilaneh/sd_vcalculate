# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
import jdatetime
import json


class SdVcalculate(models.Model):
    _name = 'sd_vcalculate.data'

    def calculate(self, function_name, diagram_id):
        print(f'------>  Calculate: {function_name} diagram_id: {diagram_id}')
        return {}



#     @api.onchange('update')
#     def update_compute(self):
#         for rec in self:
#             self._compute_values()
#         return super(KmDataPetronad, self).update_compute()
#
#     def _compute_values(self):
#         # todo: user might needed to have report based on time duration
#         productions = self.env['km_data.production'].search([('production_date', '>=' , date.today() - timedelta(days=60))])
#         meg_production = sum([rec.meg_production for rec in productions])
# #        todo: diagram id



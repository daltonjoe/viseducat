# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class viseducat_library(models.Model):
#     _name = 'viseducat_library.viseducat_library'
#     _description = 'viseducat_library.viseducat_library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

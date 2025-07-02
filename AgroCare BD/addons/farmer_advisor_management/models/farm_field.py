# -*- coding: utf-8 -*-
from odoo import models, fields

class FarmField(models.Model):
    _name = 'farm.field'
    _description = 'Farmer Field'

    name = fields.Char(string='Field Name/Identifier', required=True)
    farmer_id = fields.Many2one('farm.farmer', string='Farmer', required=True)
    location = fields.Char(string='Location (e.g., GPS Coordinates)')
    size = fields.Float(string='Size (in acres)')
    current_crop = fields.Char(string='Current Crop')
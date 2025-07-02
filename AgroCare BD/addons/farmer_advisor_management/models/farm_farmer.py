# -*- coding: utf-8 -*-
from odoo import models, fields

class FarmFarmer(models.Model):
    _name = 'farm.farmer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Farmer Record'

    name = fields.Char(string='Farmer Name', required=True, tracking=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    image = fields.Image(string='Photo')
    field_ids = fields.One2many('farm.field', 'farmer_id', string='Fields')
    field_count = fields.Integer(compute='_compute_field_count', string='Field Count')

    def _compute_field_count(self):
        for farmer in self:
            farmer.field_count = len(farmer.field_ids)
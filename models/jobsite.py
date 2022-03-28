from odoo import api, fields, models


class Jobsite(models.Model):
    _name = 'jobsite'
    _description = "Jobsite"

    name = fields.Char(string='Site Name', required=True, translate=True)
    type = fields.Selection([
        ('General', 'General'),
        ('IW', 'IWM'),
        ('T', 'Transport'),
        ('B&F', 'B&F'),
        ('FR', 'FR'),
    ], required=True, default='General',
        help="")
    status = fields.Selection([
        ('Virgin', 'Virgin'),
        ('Active', 'Active'),
        ('Closed', 'Closed'),
        ], string="Status",
        required=True, default='Virgin', help="")
    note = fields.Text(string='Description')
    active = fields.Boolean(string='isActive', default=True)
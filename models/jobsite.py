from odoo import api, fields, models


class Jobsite(models.Model):
    _name = 'jobsite'
    _inherit =['mail.thread', 'mail.activity.mixin', 'format.address.mixin']
    _description = "Jobsite"

    name = fields.Char(string='Site Name', required=True, translate=True, tracking=True)
    type = fields.Selection([
        ('General', 'General'),
        ('IWM', 'IWM'),
        ('T', 'Transport'),
        ('B&F', 'B&F'),
        ('FR', 'FR'),
    ], required=True, default='General',
        help="", tracking=True)
    status = fields.Selection([
        ('Virgin', 'Virgin'),
        ('Active', 'Active'),
        ('Closed', 'Closed'),
        ], string="Status",
        required=True, default='Virgin', help="", tracking=True)
    note = fields.Text(string='Description')
    active = fields.Boolean(string='isActive', default=True, tracking=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code = fields.Char(related='country_id.code', string="Country Code")
    latitude = fields.Float(string='Geo Latitude', digits=(10, 7))
    longitude = fields.Float(string='Geo Longitude', digits=(10, 7))
    user_ids = fields.One2many('res.users', 'partner_id', string='Users', auto_join=True)
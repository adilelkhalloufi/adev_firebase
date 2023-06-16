from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
class AdevSettings(models.Model):
    _name = 'adev.settings'
    _description = "Firebase Settings"
 
    name = fields.Char('Name Application',required=True)
    server_token = fields.Char('Server Token',required=True)


            
        
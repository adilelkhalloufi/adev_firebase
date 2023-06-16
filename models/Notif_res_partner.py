from odoo import _, api, fields, models

class MyResPartner(models.Model):
   _inherit = "res.partner"

   client_token = fields.Text('Client Token')
    
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import requests
import re

class AdevFireBaseNotfcation(models.Model):
    _name = 'adev.firebase'
    _description = "Firebase Notfcation"
    
    name = fields.Char('Name',required=True)
    title = fields.Text('Title',required=True)
    body = fields.Text('Body',required=True,default='My Bodu Notfcation ')

    listfields = fields.Selection(selection='_get_partner_fields',string='Fields', multi=True)

    @api.model
    def _get_partner_fields(self):
        partner_fields = self.env['res.partner']._fields
        return [(field, field) for field in partner_fields]

    @api.onchange('listfields')
    def _onchange_example(self):
        self.body += " {" + str(self.listfields) + "}"
        

   
    @api.model_create_multi
    def create(self, var_list):
       self.env['adev.firebase'].loop_through_all_partners(var_list[0]["title"],var_list[0]["body"])
       return super(AdevFireBaseNotfcation,self).create(var_list)


    def write(self, vals):
        res = super(AdevFireBaseNotfcation, self).write(vals)
        existing_values = self.read(list(self._fields.keys()))[0]
        self.env['adev.firebase'].loop_through_all_partners(existing_values["title"],existing_values["body"])
        print('is updated')
        return res

    @api.model
    def loop_through_all_partners(self,Thetitle,Thebody):

        print("Thetitle ",Thetitle)
        print("Thebody ",Thebody)
        settings = self.env['adev.settings'].search([], limit=1)
        if settings:
            server_token = settings[0].server_token
            Partner = self.env['res.partner']
            partners = Partner.search([])
            for partner in partners:
                if partner.client_token and isinstance(partner.client_token, str) and partner.client_token.strip():
                        print('client_token has a non-empty string value:', partner.client_token)
                        # print('title :',Thetitle)
                        # print("object name ",partner["name"])
                        # print('replace_placeholder :',self.env['adev.firebase'].replace_placeholder(Thebody,partner))
                        
                        

                        self.env['adev.firebase'].send_firebase_notification(
                            server_token,
                            partner.client_token,
                            self.env['adev.firebase'].replace_placeholders(Thetitle,partner),
                            self.env['adev.firebase'].replace_placeholders(Thebody,partner)
                            )
                else:
                    pass  



    def send_firebase_notification(self,server_key, device_token, title, body):
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {
            'Authorization': 'key=' + server_key,
            'Content-Type': 'application/json'
        }
        data = {
            'to': device_token,
            'notification': {
                'title': title,
                'body': body
            }
        }
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print('Notification sent successfully.')
        else:
            print('Failed to send notification. Error:', response.text)
      

  
   

    def replace_placeholders(self,string,partner):
        pattern = r"{(\w+)}"
        placeholder_names = re.findall(pattern, string)
      
        for field in placeholder_names:
            string = string.replace('{' + field + '}',partner[field])
        return string

       

 
            
        
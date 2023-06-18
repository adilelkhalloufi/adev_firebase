from odoo import http
import json

class OdooController(http.Controller):

     @http.route('/GetNotfcationList', auth='public', website=True)
     def GetNotfcationList(self, **kwargs):
        my_model_records = http.request.env['adev.firebase'].sudo().search([])
        data = []
        for record in my_model_records:
            data.append({
                'name': record.name,
            })
        return http.Response(json.dumps({
         "FireBaseNotifcation" : data
         }), content_type='application/json')
   
   
   
   
     @http.route('/AddNotfcation', auth='public', website=True,methods=['POST'],csrf=False)
     def AddNotfcation(self, **kwargs):
      #   data = json.loads(http.request.httprequest.data)
      if 'name' in http.request.params:
         # Key 'name' exists in the dictionary
         name_value = http.request.params['name']
         return http.Response(json.dumps({
         "Succes" : name_value
         }), content_type='application/json')
      else:
         return http.Response(json.dumps({
         "message" : "Theris no name here"
         }), content_type='application/json')
   

 

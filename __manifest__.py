{
    'name': 'Adev Firebase',
    'version': '1.0',
    'description': 'This module allows you to send notifications from Odoo to users',
    'summary': 'Send notifications from Odoo',
    'author': 'adev',
    'sequence': 5,
    'website': 'https://adev.ma/',
    'category': 'Extra Tools , Customer Relationship Management (CRM) , Communication ,Website,Productivity',
    'depends': [
        'base','contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/FRNotfcation.xml',
        'views/Notif_res_partner_view.xml',
        'views/settings.xml'
     
    ],

    'application': True,
 
}
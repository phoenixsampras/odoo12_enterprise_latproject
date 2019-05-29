# -*- coding: utf-8 -*-
from odoo.tools.translate import _
from odoo import http
from odoo import http
from odoo.http import request
from tabulate import tabulate
import json
import sys
import yaml
import logging
_logger = logging.getLogger(__name__)

from werkzeug import urls
from werkzeug.wsgi import wrap_file


class webservice(http.Controller):
    @http.route('/webservice/stock1', auth='public', methods=['POST'], type="json", csrf=False)
    def index(self, **kw):
        # request.env['messages']
        #data = yaml.load(request.httprequest.data)
        # data = yaml.load(data)
        #print ("\n\n\n\n\n\n\n\n\n\n\ndata{}".format(kw))        

        # obtener datos del de movimientos de inventario
        stock_picking_model = request.env['stock.picking']
        stock_picking_ids = stock_picking_model.sudo().search([], limit=10)
        #if 'rmStockProductos' in data:


        json_dict = {"stock_picking":[]}
        for stock_picking in stock_picking_ids:
            sp = { stock_picking.id:[{
                    "id":stock_picking.id,
                    "origin":stock_picking.origin,
                    "state":stock_picking.state,
                    "partner":stock_picking.partner_id.name
                    }
                    ]
                }
            json_dict["stock_picking"].append(sp)
        return json.dumps(json_dict)

        # print (json.dumps(kw))
        # if 'messages' in data:
        #     if not data['messages'][0]['fromMe']:
        #         as_phone = data['messages'][0]['author']
        #         as_phone = as_phone.replace("@c.us","")
        #         #  float(data['messages'][0]['chatId'])
        #         as_whatsapp_chat_id = data['messages'][0]['chatId']
        #         print (as_whatsapp_chat_id)
        #         print (as_phone)

        #         # obtener datos del cliente existente
        #         partner_model = request.env['res.partner']
        #         partner_ids = partner_model.sudo().search([['as_ws_chat_id','=',as_whatsapp_chat_id],['customer', '=', True]])
        #         # partner_list = {'status': 1, 'data': []}
        #         message = data['messages'][0]['body']
        #         try:
        #             if partner_ids:
        #                 for partner in partner_ids:

        #                     table = [['Mensaje Recibido',message,data['messages']]]
        #                     headers = ["Accion", "Mensaje","Codigo"]
        #                     table = tabulate(table, headers, tablefmt='html')
        #                     table = table.replace("<table>","<table class='blueTable'")
        #                     partner.message_post(body=table)
        #                     print (partner.name)
        #                     # return json.dumps(partner)
        #         except:
        #             print("error ")
                # return ({"isSuccess":False, "error":e})
            # self.as_save_partner_data(data)
            # return "Datos Recibidos: {}".format(data) 


    

# class as_JsonRequest(http.JsonRequest):
#     def __init__(self, *args):
#         super(as_JsonRequest, self).__init__(self, *args)
#         self.httprequest.data = request

# as_JsonRequest
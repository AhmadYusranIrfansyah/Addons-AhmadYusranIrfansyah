from odoo import http, fields, models
from odoo.http import request
import json


class StudioCon(http.Controller):
    @http.route(['/paket','/paket/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getPaket(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            paket = request.env['studio.list'].search([])            
            for p in paket:
                value.append({"id": p.id,
                            "nama_paket" : p.name,
                            "nama_photographer" : p.photo_id.name,
                            "nama_videographer" : p.video_id.name,
                            "harga_sewa" : p.harga})
            return json.dumps(value)
        else:
            paketid = request.env['studio.list'].search([('id','=',idnya)])
            for p in paketid:
                value.append({"id": p.id,
                            "nama_paket" : p.name,
                            "nama_photographer" : p.photo_id.name,
                            "nama_videographer" : p.video_id.name,
                            "harga_sewa" : p.harga})
            return json.dumps(value)
    
    @http.route('/createpaket',auth='user', type='json', methods=['POST'])
    def createKursi(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name': kw['name'], 
                    'photo_id' : kw['photo_id'],
                    'video_id' : kw['video_id'],
                    'harga' : kw['harga'],
                }
                paketbaru = request.env['studio.list'].create(vals)
                args = {'success': True, 'ID':paketbaru.id}
                return args
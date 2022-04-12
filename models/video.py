from odoo import api, fields, models


class Video(models.Model):
    _name = 'studio.video'
    _description = 'Data tentang video dan harganya'

    name = fields.Char(string='Name')
    status = fields.Selection(string='Status Videographer', selection=[('full-time','Full-time'),  ('freelance','Freelance')])
    harga = fields.Integer(string='Harga Sewa')
    
    
    

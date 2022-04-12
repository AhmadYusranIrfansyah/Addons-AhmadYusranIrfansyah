from odoo import api, fields, models


class Photo(models.Model):
    _name = 'studio.photo'
    _description = 'Data tentang photo dan harganya'

    name = fields.Char(string='Name')
    status = fields.Selection(string='Status Photographer', selection=[('full-time','Full-time'),  ('freelance','Freelance')])
    harga = fields.Integer(string='Harga Sewa')
    
    
    

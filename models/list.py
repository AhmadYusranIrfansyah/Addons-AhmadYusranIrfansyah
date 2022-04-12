from odoo import api, fields, models


class List(models.Model):
    _name = 'studio.list'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    photo_id = fields.Many2one(comodel_name='studio.photo', 
                                string='Nama Photographer')   
    video_id = fields.Many2one(comodel_name='studio.video', 
                                        string='Nama Videographer')
    
    
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    
    @api.depends('photo_id','video_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.photo_id.harga + record.video_id.harga 

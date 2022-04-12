from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'studio.order'
    _description = 'New Description'

    orderlistdetail_ids = fields.One2many(
        comodel_name='studio.orderlistdetail', 
        inverse_name='order_id', 
        string='Order List')
    
    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan',default=fields.Datetime.now())
    tanggal_kerja = fields.Date(string='Tanggal Kerja', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya','=', True)],store=True)
        
    
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('orderlistdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['studio.orderlistdetail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = a

    @api.model
    def create(self,vals):
        record = super(Order, self).create(vals) 
        if record.tanggal_pesan:
            self.env['studio.akunting'].create({'kredit' : record.total, 'name':record.name})          
            return record
    
    
    
            

class OrderListDetail(models.Model):
    _name = 'studio.orderlistdetail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='studio.order', string='Order')
    list_id = fields.Many2one(comodel_name='studio.list', string='List')   
    
         
    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='harga')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga')
    
    @api.depends('list_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.list_id.harga
    
    
    @api.depends('harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan


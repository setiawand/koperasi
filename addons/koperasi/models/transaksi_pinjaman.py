from odoo import models, fields, api


class Transaksi_pinjaman(models.Model):
    _name = 'transaksi.pinjaman'
    _description = 'tabel transaksi pinjaman'

    anggota_id = fields.Many2one('res.partner', string="Anggota", readonly=False)
    tanggal_transaksi = fields.Date(string='Tanggal Transaksi')
    kode_pinjaman = fields.Many2one('pinjaman', string="Jenis Pinjaman", readonly=False)
    nominal = fields.Float(string='nominal')
    saldo = fields.Float(string='saldo')    
    bukti_transfer = fields.Char(string='Bukti transfer')
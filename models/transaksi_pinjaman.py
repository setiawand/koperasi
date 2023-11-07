from odoo import models, fields, api


class Transaksi_simpanan(models.Model):
    _name = 'transaksi.pinjaman'
    _description = 'tabel transaksi pinjaman'

    kode_anggota = fields.Char(string='Kode Anggota', required=True)
    tanggal_transaksi = fields.Date(string='Tanggal Transaksi')
    kode_pinjaman = fields.Char(string='Kode jenis pinjaman', required=True)
    nominal = fields.Float(string='nominal')
    saldo = fields.Float(string='saldo')    
    bukti_transfer = fields.Char(string='Bukti transfer')
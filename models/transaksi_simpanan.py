# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Transaksi_simpanan(models.Model):
    _name = 'transaksi.simpanan'
    _description = 'tabel transaksi simpanan'

    # kode_anggota = fields.Char(string='Kode Anggota', required=True)
    anggota_id = fields.Many2one('res.partner', string="Anggota", readonly=False)
    tanggal_transaksi = fields.Date(string='Tanggal Transaksi')
    kode_simpanan = fields.Char(string='Kode jenis simpanan', required=True)
    nominal = fields.Float(string='nominal')
    saldo = fields.Float(string='saldo')    
    bukti_transfer = fields.Char(string='Bukti transfer')

    

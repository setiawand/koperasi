# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Anggota(models.Model):
    _inherit = 'res.partner'

    kode_anggota = fields.Char(string='Kode Anggota', required=True)
    nik = fields.Char(string='NIK', required=True)
    jml_tanggungan = fields.Integer(string='Jumlah Tanggungan')
    pekerjaan = fields.Char(string='Pekerjaan')
    tanggal_masuk = fields.Date(string='Tanggal Masuk')
    status_anggota = fields.Char(string='Status Anggota')
    is_anggota = fields.Boolean(string='Anggota Koperasi?', default=False)
    

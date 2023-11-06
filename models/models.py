# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Anggota(models.Model):
     _name = 'anggota'
     _description = 'tbl_anggota'
     #_inherit = 'res.partner'

     kode_anggota = fields.Char(string='Kode Anggota', required=True)
     nama = fields.Char(string='Nama Anggota', required=True)
     tanggal_lahir = fields.Date(string='Tanggal Lahir', required=True)
     tempat_lahir = fields.Char(string='Tempat Lahir', required=True)
     jenis_kelamin = fields.Selection(
        selection=[
            ("pria", "Pria"),
            ("wanita", "Perempuan"),
        ],string='Jenis Kelamin', required=True)
     alamat = fields.Text(string='Alamat')
     pekerjaan = fields.Char(string='Pekerjaan')
     no_telp = fields.Char(string='No Telepon')
     nik = fields.Char(string='NIK', required=True)
     jml_tanggungan = fields.Integer(string='Jumlah Tanggungan')
     tanggal_masuk = fields.Date(string='Tanggal Masuk')
     status_anggota = fields.Selection(
        selection=[
            ("aktif", "Aktif"),
            ("non_aktif", "Non Aktif"),
        ],string='Status Anggota', required=True)
     is_anggota = fields.Boolean(string='Anggota Koperasi?', default=False)
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pinjaman(models.Model):
     _name = 'pinjaman'
     _description = 'tbl_pinjaman'
     #_inherit = 'res.partner'

     kode_pinjaman = fields.Char(string='Kode Pinjaman', required=True)
     nama_pinjaman = fields.Char(string='Nama Jenis Pinjaman', required=True)
     keterangan = fields.Text(string='Alamat')
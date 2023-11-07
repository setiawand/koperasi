# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JenisSimpanan(models.Model):
    _name = 'simpanan'
    _description = 'jenis_simpanan'

    kode_simpanan = fields.Char(string='Kode Simpanan', required=True)
    nama_simpanan = fields.Char(string='Nama', required=True)
    keterangan = fields.Text()
    
    

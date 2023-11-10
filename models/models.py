# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Anggota(models.Model):
    _inherit = 'res.partner'

    kode_anggota = fields.Char(string='Kode Anggota', required=True, readonly=True)
    nik = fields.Char(string='NIK', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir', required=True)
    tempat_lahir = fields.Char(string='Tempat Lahir', required=True)
    jenis_kelamin = fields.Selection(
        selection=[
            ("pria", "Pria"),
            ("wanita", "Perempuan"),
        ],string='Jenis Kelamin', required=True)
    pekerjaan = fields.Char(string='Pekerjaan')
    jml_tanggungan = fields.Integer(string='Jumlah Tanggungan')
    tanggal_masuk = fields.Date(string='Tanggal Masuk')
    status_anggota = fields.Selection(
        selection=[
            ("aktif", "Aktif"),
            ("non_aktif", "Non Aktif"),
        ],string='Status Anggota', required=True)
    is_anggota = fields.Boolean(string='Anggota Koperasi?', default=False)

    @api.model
    def create(self, vals):
        vals['kode_anggota'] = self.env['ir.sequence'].next_by_code('anggota') or _('New')

        return super(Anggota, self).create(vals)
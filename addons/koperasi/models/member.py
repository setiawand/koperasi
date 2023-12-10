# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    member_number = fields.Char(string='Nomor Anggota', readonly=True, copy=False, default=lambda self: self._generate_nomor_anggota())
    # registration_code = fields.Char(string='Kode Pendaftaran', readonly=True, copy=False)
    nik = fields.Char(string='NIK', required=True)
    user_id = fields.Many2one('res.users', string='Pengguna', copy=False)
    birthplace = fields.Char(string='Tempat Lahir')
    birthdate = fields.Date(string='Tanggal Lahir')
    gender = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan')
    ], string='Jenis Kelamin')
    kecamatan = fields.Char(string='Kecamatan')
    kelurahan = fields.Char(string='Kelurahan/Desa')
    is_approved = fields.Boolean(string='Disetujui', default=False)
    date_approved = fields.Date(string='Tanggal Approve')
    is_member = fields.Boolean(string='Anggota Koperasi', default=False)
    status_anggota = fields.Selection(
        selection=[
            ("aktif", "Aktif"),
            ("non_aktif", "Non Aktif"),
        ],string='Status Anggota', required=True, default='aktif')

    @api.model
    def _generate_nomor_anggota(self):
        # Menghasilkan nomor anggota sesuai dengan sequence saat membuat record baru
        return self.env['ir.sequence'].next_by_code('koperasi.member.sequence')

    @api.model
    def create(self, vals):
        # vals['registration_code'] = self.env['ir.sequence'].next_by_code('koperasi.member') or '/'
        vals['member_number'] = self.env.ref('koperasi.member.sequence').next_by_id() or '/'
        
        return super(ResPartner, self).create(vals)
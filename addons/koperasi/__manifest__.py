# -*- coding: utf-8 -*-
{
    'name': "koperasi",

    'summary': """
        Aplikasi Manajemen Koperasi KPI""",

    'description': """
        Aplikasi ini cocok digunakan oleh lembaga Koperasi dengan skala kecil, menengah dan besar
    """,

    'author': "Sekolahan Indonesia Digital",
    'website': "https://learning.sekolahan.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/views.xml'
        # 'views/templates.xml',
        # 'views/views_jenissimpanan.xml',
        # 'views/views_transaksi_simpanan.xml',
        # 'views/pinjaman.xml',
        # 'views/views_transaksi_pinjaman.xml',
        # 'wizard/anggota_report_wizard.xml',
        # 'reports/anggota_report_view.xml',
        # 'reports/anggota_reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'maintainer': 'Sekolahan Indonesia Digital',
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}

from odoo import api, models


class ReportSalesSalespersonWise(models.AbstractModel):
    _name = 'report.tac_module.sale_tac_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'data': data['form'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],
        }
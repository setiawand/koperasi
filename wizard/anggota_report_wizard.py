from odoo import models, fields, api, _

import logging
import pytz

_logger = logging.getLogger(__name__)

class AnggotaReport(models.TransientModel):
    _name = 'anggota.report'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    def print_report(self):
        sales_order = self.env['sale.order'].sudo().search([])
        sale_order_groupby_dict = {}
        for salesperson in self.salesperson_ids:
            filtered_sale_order = list(filter(lambda x: x.user_id == salesperson, sales_order))
            filtered_by_date = list(filter(lambda x: x.date_order >= self.start_date and x.date_order <= self.end_date, filtered_sale_order))
            sale_order_groupby_dict[salesperson.name] = filtered_by_date

        final_dist = {}
        for salesperson in sale_order_groupby_dict.keys():
            sale_data = []
            for order in sale_order_groupby_dict[salesperson]:
                temp_data = []
                temp_data.append(order.name)
                temp_data.append(order.date_order)
                temp_data.append(order.partner_id.name)
                temp_data.append(order.amount_total)
                sale_data.append(temp_data)
            final_dist[salesperson] = sale_data
        
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
        start_date = pytz.utc.localize(self.start_date).astimezone(user_tz)
        end_date = pytz.utc.localize(self.end_date).astimezone(user_tz)

        datas = {
            'ids': self,
            'model': 'sale.salesperson.report',
            'form': final_dist,
            'start_date': start_date,
            'end_date': end_date
        }
        return self.env.ref('koperasi.action_anggota_report').report_action([], data=datas)
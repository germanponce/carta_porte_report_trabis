# -*- coding: utf-8 -*-
# Coded by German Ponce Dominguez 
#     ▬▬▬▬▬.◙.▬▬▬▬▬  
#       ▂▄▄▓▄▄▂  
#    ◢◤█▀▀████▄▄▄▄▄▄ ◢◤  
#    █▄ █ █▄ ███▀▀▀▀▀▀▀ ╬  
#    ◥ █████ ◤  
#     ══╩══╩═  
#       ╬═╬  
#       ╬═╬ Dream big and start with something small!!!  
#       ╬═╬  
#       ╬═╬ You can do it!  
#       ╬═╬   Let's go...
#    ☻/ ╬═╬   
#   /▌  ╬═╬   
#   / \
# Cherman Seingalt - german.ponce@outlook.com

from odoo import api, fields, models, _, tools, SUPERUSER_ID
from odoo.exceptions import UserError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit ='account.invoice'

    def get_account_tax_ret(self):
        TotalImpuestosTrasladados = 0
        TotalImpuestosRetenidos = 0
        for line_tax_id in self.tax_line_ids:
            line_tax_id_amount = abs(line_tax_id.amount or 0.0)
            if line_tax_id.amount >= 0:
                TotalImpuestosTrasladados += line_tax_id_amount
            else:
                TotalImpuestosRetenidos += line_tax_id_amount
        return TotalImpuestosRetenidos

    def get_account_tax_trasl(self):
        TotalImpuestosTrasladados = 0
        TotalImpuestosRetenidos = 0
        for line_tax_id in self.tax_line_ids:
            line_tax_id_amount = abs(line_tax_id.amount or 0.0)
            if line_tax_id.amount >= 0:
                TotalImpuestosTrasladados += line_tax_id_amount
            else:
                TotalImpuestosRetenidos += line_tax_id_amount
        return TotalImpuestosTrasladados
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

{
    'name': 'Formato Factura - Grupo SLS',
    'category': 'LdM',
    'description': """

        Agrega Modificaciones al Reporte: 
         * Factura

    """,
    'author': 'German Ponce Dominguez',
    'website': 'https://argil.mx',
    "support": "german.ponce@argil.mx",
    'depends': [
                    'account',
                    'l10n_mx_einvoice',
                    'l10n_mx_einvoice_waybill_complemento_ce',
                ],
    'data': [
        'account_view.xml',
        'report/account_report_pdf.xml',
        ],
    'installable': True,
}
# Copyright 2021 Binovo IT Human Project SL
# Copyright 2022 Landoo Sistemas de Informacion SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "TicketBAI - Point of Sale - "
    "declaración de todas las operaciones de venta realizadas por las personas "
    "y entidades que desarrollan actividades económicas",
    "version": "14.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/OCA/l10n-spain",
    "author": "Binovo," "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
    "development_status": "Beta",
    "maintainers": ["ao-landoo"],
    "depends": ["l10n_es_pos", "l10n_es_ticketbai"],
    "data": [
        "security/ir.model.access.csv",
        "views/l10n_es_ticketbai_pos.xml",
        "views/l10n_es_ticketbai_pos_views.xml",
        "views/pos_order_views.xml",
        "views/ticketbai_certificate_views.xml",
    ],
    "qweb": ["static/src/xml/pos.xml"],
}

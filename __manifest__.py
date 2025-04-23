# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Point of Sale Invoice Wizard",
    "summary": "This module allows selecting in a wizard the journal to invoice all pos_orders you need to invoice after closing session.",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "17.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["point_of_sale", "account"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/pos_order_invoice_wizard_view.xml",
        "views/pos_order_view_inherit.xml",
    ],
}

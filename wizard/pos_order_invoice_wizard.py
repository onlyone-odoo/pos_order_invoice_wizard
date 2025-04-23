from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PosOrderInvoiceWizard(models.TransientModel):
    _name = "pos.order.invoice.wizard"
    _description = "Wizard para Facturar Pedido PoS con Diario Personalizado"

    journal_id = fields.Many2one(
        "account.journal",
        string="Diario",
        required=True,
        domain="[('type', '=', 'sale'), ('company_id', '=', company_id)]",
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañía",
        required=True,
        default=lambda self: self.env.company.id,
    )

    def action_invoice_with_custom_journal(self):
        # Obtener los pedidos seleccionados
        pos_orders = self.env["pos.order"].browse(
            self.env.context.get("active_ids", [])
        )
        if not pos_orders:
            raise UserError(_("No se seleccionaron pedidos."))

        # Llamar al método personalizado para facturar con el diario seleccionado
        return pos_orders.action_pos_order_invoice_custom_journal(self.journal_id.id)

from odoo import models, api
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = "pos.order"

    def action_pos_order_invoice_custom_journal(self, journal_id):
        if len(self.company_id) > 1:
            raise UserError(_("No puedes facturar pedidos de diferentes compañías."))
        self.write({"to_invoice": True})
        if (
            self.company_id.anglo_saxon_accounting
            and self.session_id.update_stock_at_closing
            and self.session_id.state != "closed"
        ):
            self._create_order_picking()
        return self._generate_pos_order_invoice_custom_journal(journal_id)

    def _generate_pos_order_invoice_custom_journal(self, journal_id):
        moves = self.env["account.move"]

        for order in self:
            # Forzar compañía para todas las acciones de SUPERUSER_ID
            if order.account_move:
                moves += order.account_move
                continue

            if not order.partner_id:
                raise UserError(_("Por favor, proporciona un cliente para la venta."))

            # Preparar los valores de la factura
            move_vals = order._prepare_invoice_vals()
            # Sobreescribir el journal_id con el seleccionado
            move_vals["journal_id"] = journal_id
            new_move = order._create_invoice(move_vals)

            order.write({"account_move": new_move.id, "state": "invoiced"})
            new_move.sudo().with_company(order.company_id).with_context(
                skip_invoice_sync=True
            )._post()

            moves += new_move
            payment_moves = order._apply_invoice_payments(
                order.session_id.state == "closed"
            )

            # Enviar y generar PDF
            if self.env.context.get("generate_pdf", True):
                template = self.env.ref(new_move._get_mail_template())
                new_move.with_context(
                    skip_invoice_sync=True
                )._generate_pdf_and_send_invoice(template)

            if order.session_id.state == "closed":
                order._create_misc_reversal_move(payment_moves)

        if not moves:
            return {}

        return {
            "name": _("Factura de Cliente"),
            "view_mode": "form",
            "view_id": self.env.ref("account.view_move_form").id,
            "res_model": "account.move",
            "context": "{'move_type':'out_invoice'}",
            "type": "ir.actions.act_window",
            "target": "current",
            "res_id": moves and moves.ids[0] or False,
        }

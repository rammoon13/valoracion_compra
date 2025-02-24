# valoracion_compra/models/valoracion_compra.py
from odoo import models, fields, api

class ValoracionCompra(models.Model):
    _name = 'valoracion.compra'
    _description = 'Valoración de Compra'

    trabajador = fields.Many2one('hr.employee', string="Nombre del Trabajador", required=True)
    empresa = fields.Many2one('res.partner', string="Nombre de la Empresa", required=True, domain=[('is_company', '=', True)])
    fecha_compra = fields.Date(string="Fecha de la Compra", required=True)
    comentario = fields.Text(string="Comentario sobre el desempeño", required=True)
    linea_ids = fields.One2many('valoracion.compra.line', 'compra_id', string="Artículos Vendidos")

    @api.onchange('empresa')
    def _onchange_empresa(self):
        """Actualizar automáticamente algún campo relacionado con la empresa si es necesario"""
        if self.empresa:
            self.comentario = f"Valoración de la compra para {self.empresa.name}"

    @api.model
    def create(self, vals):
        """Este método se ejecuta al crear un nuevo registro de valoración"""
        record = super(ValoracionCompra, self).create(vals)
        return record


class ValoracionCompraLine(models.Model):
    _name = 'valoracion.compra.line'
    _description = 'Línea de Artículos Vendidos en la Valoración de Compra'

    compra_id = fields.Many2one('valoracion.compra', string="Compra", ondelete='cascade')
    producto = fields.Many2one('product.product', string="Producto", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)

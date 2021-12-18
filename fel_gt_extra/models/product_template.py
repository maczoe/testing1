from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    price_suggested = fields.Monetary('Precio sugerido')
    codigo_unidad_gravable = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    ])


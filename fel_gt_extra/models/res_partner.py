# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    postal_code = fields.Integer('Codigo postal', required=True)
    municipality = fields.Char('Municipio', required=True)
    department = fields.Char('Departamento', required=True)


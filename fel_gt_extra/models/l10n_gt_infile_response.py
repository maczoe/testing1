from odoo import models, fields, api, _

class InvoiceResponse(models.Model):
    _inherit = "account.move"

    id = fields.Id()
    result = fields.Boolean(False)
    date_transaction = fields.Date()
    origin = fields.Text()
    description = fields.Text()
    emition_control = fields.Text()
    infile_alert = fields.Boolean
    infile_alert_description = fields.Text()
    sat_alert = fields.Boolean()
    sat_alert_description = fields.Text()
    errors = fields.Integer()
    error_description = fields.Text()
    aditional_information = fields.Text()
    uuid = fields.Text()
    serie = fields.Text()
    number = fields.Integer()
    xml_certificado = fields.Text()


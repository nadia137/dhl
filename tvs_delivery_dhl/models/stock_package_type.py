from odoo import fields, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection([
        ('dhl', 'DHL'),
    ], string="Carrier Type")
    shipper_package_code = fields.Char(string="Shipper Package Code")
    dhl_default_package_type_id = fields.Many2one('stock.package.type', string='DHL Package Type')


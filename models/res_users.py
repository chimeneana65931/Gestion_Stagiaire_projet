from odoo import models, fields
class ResUsers(models.Model):
    _inherit = 'res.users'

    is_stagiaire = fields.Char(string='Stagiaire',store=True)
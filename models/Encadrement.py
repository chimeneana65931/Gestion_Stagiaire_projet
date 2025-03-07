from odoo import fields, models
class Encadrement(models.Model):
   _name = 'encadrement'
   Stagiaire = fields.Many2one('res.users', string='Stagiaire')
   Encadreur = fields.Many2one('res.users', string='Encadreur')


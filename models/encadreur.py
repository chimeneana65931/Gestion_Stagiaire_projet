from odoo import models, fields

class Encadreur(models.Model):
   _name = 'encadreur'

   id_encadreur = fields.Integer('ID encadreur', required=True)
   nom = fields.Char(string='Nom', required=True)
   email = fields.Char('email', required=True)
   telephone = fields.Integer('telephone', required=True)








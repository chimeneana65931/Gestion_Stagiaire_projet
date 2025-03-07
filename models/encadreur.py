from odoo import models, fields

class Encadreur(models.Model):
   _name = 'encadreur'

   # Champ Many2one pour lier chaque stagiaire à un encadreur
  # encadreur_id = fields.Many2one('hr.employee', string='Encadreur', domain="[('job_id.name', '=', 'Encadreurs')]")



   #id_encadreur = fields.Integer('ID encadreur', required=True)
   #nom = fields.Char(string='Nom', required=True)
   #email = fields.Char('email', required=True)
   #telephone = fields.Integer('telephone', required=True)








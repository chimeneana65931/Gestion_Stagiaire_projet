from odoo import models, fields
class Projet(models.Model):
    _name = 'projet'

    name = fields.Char(string="Project Name", required=True)
    description = fields.Text(string="Description", required=True)
    date_debut = fields.Date(string="Start Date", required=True)
    date_fin = fields.Date(string="End Date", required=True)

    # Ajout du champ stagiaire_id pour la relation avec le modèle stagiaire
    stagiaire_id = fields.Many2one('gestion_stagiaire.stagiaire', string="Stagiaire")




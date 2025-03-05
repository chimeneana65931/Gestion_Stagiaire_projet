from odoo import models, fields, api

class Attestation(models.Model):
    _name = 'attestation'
    Commentaire = fields.Char('Nous reconnaissons avoir admis(e) en stage M/Mlle')
    nom_stagiaire = fields.Many2one('gestion_stagiaire.stagiaire', string="Stagiaire")
    nom_entreprise = fields.Char(String='Nom  de l\entreprise')
    duree_stage = fields.Char(String="Durée stage")
    projet = fields.Char(String="Projet réalisé")

    @api.depends('nom_stagiaire', 'nom_entreprise', 'duree_stage', 'projet')
    def _compute_commentaire(self):
        for record in self:
            if record.nom_stagiaire and record.nom_entreprise and record.duree_stage and record.projet:
                record.Commentaire = f"Nous reconnaissons avoir admis(e) {record.nom_stagiaire.name} en stage au sein de {record.nom_entreprise}, pour une durée de {record.duree_stage}, avec le projet {record.projet}."
            else:
                record.Commentaire = ''



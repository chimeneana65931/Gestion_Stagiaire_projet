from odoo import models, fields, api

class Evaluation(models.Model):
    _name = 'evaluation'

    # Date de l'évaluation
    date_evaluation = fields.Date(string="Date de l'évaluation", required=True, default=fields.Date.today)

    #Critères d'évaluation (exemple : Assiduité, Compétences, Engagement, etc.)
    assiduite = fields.Integer(string="Assiduité", required=True)
    competences = fields.Integer(string="Compétences", required=True)
    engagement = fields.Integer(string="Engagement", required=True)
    note_globale = fields.Float(string="Note Globale", compute="_compute_note_globale", store=True)

    # Commentaires sur l'évaluation
    commentaire = fields.Text(string="Commentaire de l'encadreur")

    # Calcul de la note globale
    @api.depends('assiduite', 'competences', 'engagement')
    def _compute_note_globale(self):
        for record in self:
         record.note_globale = (record.assiduite + record.competences + record.engagement) / 3

    groups_id = fields.Many2many('res.groups', string='Groupes')

    stagiaire_id = fields.Many2one('gestion.stagiaire', string='Stagiaire')
    date = fields.Date('Date')
    note = fields.Float('Note')
    commentaire = fields.Text('Commentaire')

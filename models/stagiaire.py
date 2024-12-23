
from odoo import models, fields


# class ResUsers(models.Model):
  #  _inherit = 'res.users'

    # is_stagiaire = fields.Boolean(string="Stagiaire ?", store=True)
    #
    # entreprise_accueil = fields.Char(string='Entreprise d\'accueil',store=True)
    # tuteur = fields.Char(string='Tuteur',store=True)
    # date_debut_stage = fields.Date(string='Date de début du stage',store=True)
    # date_fin_stage = fields.Date(string='Date de fin du stage',store=True)
    # duree_stage = fields.Integer(string='Durée du stage (mois)',store=True)

class Stagiaire(models.Model):
    _name = 'gestion.stagiaire'
    _description = 'Stagiaire'

    # Ajouter des informations spécifiques au stagiaire
    name = fields.Char(string='Nom du stagiaire')
    entreprise_accueil = fields.Char(string='Entreprise d\'accueil')
    tuteur = fields.Char(string='Tuteur')
    date_debut_stage = fields.Date(string='Date de début')
    date_fin_stage = fields.Date(string='Date de fin')
    duree_stage = fields.Integer(string='Durée du stage (mois)')

    user_id = fields.Many2one('res.users', string='Utilisateur', ondelete='cascade')

    def create_stagiaire_from_user(self):
        """
        Créer un stagiaire à partir d'un utilisateur
        """
        for user in self:
            self.create({
                'name': user.name,
                'entreprise_accueil': user.entreprise_accueil,
                'tuteur': user.tuteur,
                'date_debut_stage': user.date_debut_stage,
                'date_fin_stage': user.date_fin_stage,
                'duree_stage': user.duree_stage,
                'user_id': user.id,
            })



#class Stagiaire(models.Model):
     #_inherit = 'res.users'
    #_name = 'gestion.stagiaire'
    #_description = 'Stagiaire'
    # name = fields.Char('Nom', required=True)
    #date_naissance = fields.Date('Date de naissance')
    #email = fields.Char('Email')
    #telephone = fields.Char('Téléphone')
    #encadreur_id = fields.Many2one('encadreur',  string='Encadreurs')
    #projet_ids = fields.One2many('projet', 'stagiaire_id', string='Projets')
    #evaluation_ids = fields.One2many('evaluation', 'stagiaire_id', string='Évaluations')
    #theme_ids = fields.One2many('theme', 'stagiaire_id', string='Thèmes')
    #presence_ids = fields.One2many('presence', 'stagiaire_id', string='Présences')



     #class HrIntern(models.Model):
        # _name = 'hr.intern'
         #_description = 'Intern'

         #name = fields.Char('Full Name', required=True)
         #email = fields.Char('Email')
         #phone = fields.Char('Phone')
         #school = fields.Char('School')
         #specialty = fields.Char('Specialty')

         # Champ Many2one pour lier un stagiaire à un utilisateur (par exemple, le responsable)
         #user_id = fields.Many2one('res.users', string='Assigned User', help="User assigned to the intern")


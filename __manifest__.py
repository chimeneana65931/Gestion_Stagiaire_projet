{
    'name': 'Gestion Stagiaires',
    'version': '17.0',
    'category': 'Human Resources',
    'summary': 'Module de gestion des stagiaires avec encadreurs, projets, evaluations, themes et presences.',
    'depends': ['base', 'hr_attendance','project','hr', 'hr_appraisal'], # Dépendances nécessaires
    'data':[
        #'security/ir.model.access.csv',
        'views/encadreur_views.xml',
        'views/projet_views.xml',
        'views/stagiaire_views.xml',
        'views/evaluation_views.xml',
        'views/attestation_views.xml',
        #'views/theme_views.xml',
        'views/encadrement.xml',
        'views/presence_views.xml',
        #'views/menu.xml',
        'views/views.xml',
        'security/security.xml',

    ],
    'installable': True,
    'application': True,
}



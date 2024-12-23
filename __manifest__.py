{
    'name': 'Gestion Stagiaires',
    'version': '17.0',
    'category': 'Human Resources',
    'summary': 'Module de gestion des stagiaires avec encadreurs, projets, evaluations, themes et presences.',
    'depends': ['base', 'hr', 'project',],
    'data':[
        'security/ir.model.access.csv',
        'views/stagiaire_views.xml',
       # 'views/encadreur_views.xml',
        #'views/projet_views.xml',
        #'views/evaluation_views.xml',
        #'views/theme_views.xml',
       # 'views/presence_views.xml',
        'views/menu.xml',

    ],
    'installable': True,
    'application': False,
}
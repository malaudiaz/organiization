{
    'name': 'Organizaciones',
    'version': '1.0.0',
    'description': """ Modulo para crear organizaciones gerarquicas por tipo """,
    'summary': """ Modulo para crear organizaciones gerarquicas por tipo """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'hr'],

    "data": [
        "views/organization_type_views.xml",
        "views/organization_organization_views.xml",
        "views/organization_members_views.xml",
        "views/organization_menuitem.xml",
        "security/ir.model.access.csv",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}


{
    'name': 'Organizaciones',
    'version': '1.0.0',
    'description': """ Modulo para crear organizaciones jerarquicas por tipo """,
    'summary': """ Modulo para crear organizaciones jerarquicas por tipo """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'hr'],

    "data": [
        "views/organization_type_views.xml",
        "views/organization_organization_views.xml",
        "views/organization_members_views.xml",
        "views/organization_country_views.xml",
        "views/organization_city_views.xml",
        "views/organization_position_views.xml",
        "views/organization_org_member_position_views.xml",
        "views/organization_menuitem.xml",
        "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/country.xml',
        'demo/city.xml',
        'demo/type.xml',
        'demo/members.xml',
        'demo/organization.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}


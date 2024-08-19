{
    'name': 'Organizaciones',
    'version': '1.0.0',
    'description': """ Modulo para crear organizaciones jerarquicas por tipo """,
    'summary': """ Modulo para crear organizaciones jerarquicas por tipo """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'hr', 'contacts', 'sale', 'membership'],
  
    "data": [
        "views/organization_type_views.xml",
        "views/organization_position_views.xml",
        "views/res_partner_views.xml",
        "views/res_company_views.xml",
        "views/organization_menuitem.xml",
        "security/ir.model.access.csv"
    ],
    
    "assets": {
        "web.assets_backend": [
            'organization/static/src/css/style.css'
        ], 
    },    
    
    # only loaded in demonstration mode
    'demo': [
        'demo/type.xml',
        'demo/position.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

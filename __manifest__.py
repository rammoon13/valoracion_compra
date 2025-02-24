# valoracion_compra/__manifest__.py
{
    'name': 'Valoración de Compra',
    'version': '1.0',
    'summary': 'Módulo para gestionar la valoración de compra de un trabajador',
    'category': 'Sales',
    'author': 'Ramon Herrera Robles',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'icon': '/valoracion_compra/static/description/icon1.png',  # Ruta del icono
    'data': [
        'security/ir.model.access.csv',
        'views/valoracion_compra_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/valoracion_compra/static/src/css/styles.css',  # Ruta del CSS
        ],
    },
    'application': True,
    'installable': True,
}


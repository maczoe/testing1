# Copyright (C) 2021 In Nova TI
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# noinspection PyStatementEffect

{
    'name': 'FEL Guatemala Extra',
    'version': '1.0',
    'category': 'customizations',
    'description': """ 	Guatemala Extra Alcoholic Beverage """,
    "license": "LGPL-3",
    'author': 'Esteban Zelada - In Nova TI',
    "maintainer": "Esteban Zelada - In Nova TI",
    'website': 'https://www.innovati.cl/',
    'depends': ['product', 'account'],
    'data': [
        'views/product_template.xml',
        # 'views/partner_view.xml',
    ],
    'installable': True,
    'application': True,
}

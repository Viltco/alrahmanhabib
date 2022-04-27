# -*- coding: utf-8 -*-
{
    'name': "Project Imports",

    'summary': """
        Open Read Create Data From XLSX File""",

    'description': """
        Open Read Create Data From XlSX File
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'project',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/task_import_wizard_views.xml',
        'views/project_views.xml',
    ],

}

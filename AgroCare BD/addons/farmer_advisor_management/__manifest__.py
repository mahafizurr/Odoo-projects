# -*- coding: utf-8 -*-
{
    'name': "Farmer Advisory Management",
    'version': '17.0.1.0',
    'summary': """
        Manage farmer visits, problems, recommendations, and reports.
    """,
    'description': """
        A comprehensive module for managing agricultural advisory services. 
        Features include:
        - Farmer and Field Management
        - Visit Scheduling with Calendar View
        - Problem and Recommendation Logging with Images
        - PDF Visit Reports
        - Survey Integration
    """,
    'author': "Your Name / Company",
    'website': "https://www.yourcompany.com",
    'category': 'Industries',
    'depends': ['base', 'mail', 'calendar', 'survey'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/farm_farmer_views.xml',
        'views/farm_field_views.xml',
        'views/farm_visit_views.xml',
        'views/menus.xml',
        'report/visit_report.xml',
        'report/visit_report_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
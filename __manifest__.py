# -*- coding: utf-8 -*-
{
    'name': "viseducat_library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'account',
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/vm_security.xml',
        # 'data/action_rule_data.xml',
        # 'data/custom_paperformat.xml',
        # 'data/media_queue_sequence.xml',
        # 'data/product_demo.xml',
        'wizards/issue_media_view.xml',
        # 'wizards/reserver_media_view.xml',
        'wizards/return_media_view.xml',
        'report/report_media_barcode.xml',
        'report/report_library_card_barcode.xml',
        'report/report_student_library_card.xml',
        'report/report_menu.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/library_view.xml',
        'views/media_view.xml',
        'views/publisher_view.xml',
        'views/author_view.xml',
        'views/media_unit_view.xml',
        'views/media_type_view.xml',
        'views/media_purchase_view.xml',
        'views/media_queue_view.xml',
        'views/media_movement_view.xml',
        'views/tag_view.xml',
        'menus/vm_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/author_demo.xml',
        'demo/library_card_demo.xml',
        'demo/library_card_type_demo.xml',
        'demo/media_demo.xml',
        'demo/media_movement_demo.xml',
        'demo/media_purchase_demo.xml',
        'demo/media_queue_demo.xml',
        'demo/media_type_demo.xml',
        'demo/media_unit_demo.xml',
        'demo/publisher_demo.xml',
        'demo/res_users_demo.xml',
        'demo/tag_demo.xml',
    ],
    'images': [
        'static/description/openeducat_library_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

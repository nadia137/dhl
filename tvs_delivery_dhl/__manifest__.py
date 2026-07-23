# -*- coding: utf-8 -*-
{
    'name': "DHL Express Shipping | DHL Shipping Connector | DHL Shipping | DHL",
    'summary': "Send your packages safely and efficiently through DHL — one of the world’s most trusted courier services. Enjoy fast, reliable, and secure delivery for all your shipments, whether local or international. You can easily track your parcels online in real-time, receive instant updates, and stay informed about every step of your delivery journey from dispatch to destination",
    'description': "Send your packages safely and efficiently through DHL — one of the world’s most trusted courier services. Enjoy fast, reliable, and secure delivery for all your shipments, whether local or international. You can easily track your parcels online in real-time, receive instant updates, and stay informed about every step of your delivery journey from dispatch to destination",
    'category': 'Inventory/Delivery',
    'sequence': 285,
    'author':"TVS Odoo Apps",
    'version': '1.0',
    'application': True,
    'depends': ['delivery', 'mail','stock'],
    'data': [
        'data/delivery_dhl_data.xml',
        'views/delivery_dhl_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'price': '99.9',
    'currency': 'USD',
    "images": ["static/description/th.png", ],
}

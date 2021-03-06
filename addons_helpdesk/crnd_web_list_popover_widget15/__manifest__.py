{
    "name": "CRND Web List Popover Widget",
    "version": "15.0.0.5.1",
    "author": "Center of Research and Development",
    "website": "https://crnd.pro",
    'summary': 'Tooltips message for text fields on tree view.',
    "license": "LGPL-3",
    'category': 'Technical Settings',
    'depends': [
        'web',
    ],
    'data': [
    ],
    'qweb': [
        "static/src/xml/popover_templates.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'crnd_web_list_popover_widget15/static/src/css/list_popover_widget.css',
            'crnd_web_list_popover_widget15/static/src/js/list_popover_mixin.js',
            'crnd_web_list_popover_widget15/static/src/js/list_text_popover_widget.js',
            'crnd_web_list_popover_widget15/static/src/js/list_char_popover_widget.js',
            'crnd_web_list_popover_widget15/static/src/js/list_html_popover_widget.js'
        ]
    },
    'images': [],
    'installable': True,
    'auto_install': False,
}

DEFAULT_CONFIG = {
    'frame_insert_html': 'frame_insert.html',
    'proxy_select_html': 'proxy_select.html',
    'static_shared_prefix': 'static/__shared',
    'framed_replay': 'inverse',
    'enable_memento': True,
    'head_insert_html': 'head_insert.html',
    'query_html': 'query.html',
    'not_found_html': 'not_found.html',
    'home_html': 'index.html',
    'banner_html': 'banner.html',
    'paths': {
        'template_files': {
            'frame_insert_html': 'frame_insert.html',
            'query_html': 'query.html',
            'not_found_html': 'not_found.html',
            'banner_html': 'banner.html',
            'search_html': 'search.html',
            'head_insert_html': 'head_insert.html'
        },
        'templates_dir': 'templates',
        'index_paths': 'indexes',
        'archive_paths': 'archive',
        'shared_template_files': {
            'proxy_select_html': 'proxy_select.html',
            'info_json': 'collinfo.json',
            'home_html': 'index.html',
            'error_html': 'error.html',
            'proxy_cert_download_html': 'proxy_cert_download.html'
        },
        'static_path': 'static'
    },
    'template_globals': {'static_path': 'static/__pywb'},
    'proxy_cert_download_html': 'proxy_cert_download.html',
    'static_routes': {'static/__pywb': 'pywb/static/'},
    'static_default_prefix': 'static/__pywb',
    'collections_root': 'collections',
    'search_html': 'search.html',
    'templates_dirs': ['templates', '.', '/'],
    'template_packages': ['pywb'],
    'error_html': 'error.html',
    'info_json': 'collinfo.json',
    'domain_specific_rules': 'pywb/rules.yaml'
}

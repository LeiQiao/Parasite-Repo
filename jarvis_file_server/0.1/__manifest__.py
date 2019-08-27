# noinspection PyStatementEffect
{
    'name': 'jarvis_file_server',
    'summary': '',
    'description': 'Jarvis File 服务端接口',

    'author': '',
    'website': '',
    'source': {'git': 'git@git.chinapnr.com:parasite/jarvis/jfile.git', 'branch': 'master'},

    'category': 'jarvis',
    'version': '0.1',

    'api': {
        '/file/v3/health': 'jarvis_file_api.health',
        '/file/v4/health': 'jarvis_file_api.health',
        '/file/v5/health': 'jarvis_file_api.health',
        '/file/v3/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v4/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v5/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v2.0.1/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v2.0.2/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v2.0.3/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v2.0.4/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v2.0.5/files': {
            'POST': 'jarvis_file_api.upload_file',
            'GET': 'jarvis_file_api.download_file',
            'DELETE': 'jarvis_file_api.delete_file'
        },
        '/file/v3/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v4/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v5/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v2.0.1/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v2.0.2/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v2.0.3/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v2.0.4/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v2.0.5/download': {'GET': 'jarvis_file_api.download_password_file'},
        '/file/v5/share/guest': {
            'POST': 'jarvis_file_api.add_share_path_guest',
            'GET': 'jarvis_file_api.get_share_path_guest',
            'DELETE': 'jarvis_file_api.delete_share_path_guest'
        },
        '/file/v5/share': {'GET': 'jarvis_file_api.get_share_path'}
    },

    # any plugin necessary for this one to work correctly
    'depends': [
        'base_api_wrapper',
        'acm_config_manager',
        'jarvis_man_client',
        'oss_client',
        'pegasus_client',
        'redis_client'
    ]
}

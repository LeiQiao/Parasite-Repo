# noinspection PyStatementEffect
{
    'name': 'JAccountUser',
    'summary': '',
    'description': '',
    'author': '',
    'website': '',
    'source': {'git': 'git@172.31.13.131:collection/collection-api.git', 'branch': 'v1.0.0_develop'},

    'category': '',
    'version': '0.1',

    'api': {
        '/login/session': 'login.session',
        '/login/captcha': 'login.captcha',
        '/login': 'login.login',
        '/permission/list': 'permission.get_all_permission',
        '/user/list': 'user.get_all_user',
        '/user': {
            'POST': 'user.add_user',
            'PUT': 'user.edit_user',
            'GET': 'user.get_user',
            # 'DELETE': 'user.delete_user'
        }
    },

    # any plugin necessary for this one to work correctly
    'depends': ['base', 'base_api_wrapper', 'redis_client']
}

# noinspection PyStatementEffect
{
    'name': 'jarvis_man_client',
    'summary': '',
    'description': 'Jarvis Man 客户端软件',

    'author': '',
    'website': '',
    'source': {'git': 'git@git.chinapnr.com:parasite/jarvis/jfile.git', 'branch': 'master'},

    'category': 'jarvis',
    'version': '0.1',

    'exports': ['JarvisManClient'],

    # any plugin necessary for this one to work correctly
    'depends': ['base', 'redis_client']
}

# noinspection PyStatementEffect
{
    'name': 'base_schedule',
    'summary': '',
    'description': '可以在 manifest 中添加定时任务并将其绑定到某个任务对象',

    'author': '',
    'website': '',
    'source': {'git': 'http://172.31.13.131:8088/parasite/Parasite-Plugins.git', 'branch': 'master'},

    'category': 'base',
    'version': '0.1',

    'exports': ['Schedule'],

    # any plugin necessary for this one to work correctly
    'depends': ['base']
}

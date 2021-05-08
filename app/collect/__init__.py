"""
@File    : __init__.py
@Time    : 2021/4/23 16:14
@Author  : shroud.xu
@Description: 一个 ctrl c + v 工程师
@Email   : shroud.xu@cygia.com
@Software: PyCharm
"""
class Collect_liaoxuefeng(object):
    from .spider_liaoxuefeng import spider_liaoxuefeng
    base_url = 'https://www.liaoxuefeng.com'
    spi = spider_liaoxuefeng()


collect = {
    'liaoxuefeng': Collect_liaoxuefeng
}


def create_collect(config_name):
    return collect[config_name]

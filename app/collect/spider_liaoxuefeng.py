"""
@File    : spider_liaoxuefeng.py
@Time    : 2021/4/23 16:14
@Author  : shroud.xu
@Description: 一个 ctrl c + v 工程师
@Email   : shroud.xu@cygia.com
@Software: PyCharm
"""
import requests
import re
import urllib3


class spider_liaoxuefeng(object):
    def get_source(self, url):
        ret = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
        }
        urllib3.disable_warnings()
        r = requests.get(url, headers=headers, verify=False)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            ret = r.text
        return ret

    def get_title(self, html):
        return re.search('(?<=<title>).*?(?=</title>)', html, re.S).group()

    def get_body(self, html):
        return re.search('(?<=<div class="x-wiki-content x-main-content">).*?(?=</div>)', html, re.S).group()

    def get_page_list(self, html):
        # url_box_temp = re.search('(?<=<ul id="x-wiki-index" class="uk-nav uk-nav-side" style="margin-right:-15px;">).*?(?=</ul>)',
        #                     html, re.S)
        # print("url_box_temp: ", url_box_temp)
        url_box = re.search(
            '(?<=<ul id="x-wiki-index" class="uk-nav uk-nav-side" style="margin-right:-15px;">).*?(?=</ul>)',
            html, re.S).group()
        url_list = re.findall('href="(.*?)" class="x-wiki-index-item">(.*?)</a>', url_box, re.S)
        new_url_list = [(url, name) for url, name in url_list]
        return new_url_list

    def get_index_list(self, html):
        category = [r'JavaScript教程', r'Python教程', r'Git教程']
        url_box = re.search('(?<=<ul id="ul-navbar" class="uk-navbar-nav uk-hidden-small">).*?(?=</ul>)',
                            html, re.S).group()
        # print("url box: ", url_box)

        url_list = re.findall('href="(.*?)"(.*?)</span> (.*?)</a>', url_box, re.S)
        # print("url list: ", url_list)
        new_url_list = []
        for url, temp, name in url_list:
            if name in category:
                new_url_list.append((url, name))
        return new_url_list

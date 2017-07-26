#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseSpider:
    """
    爬虫基类
    """

    def __init__(self, school, system='Jw'):
        self._config = self._get_config(school, system)

    def _get_config(self, school, system='Jw'):
        """
        通过学校和系统字段，返回对应的配置类。

        :param school: 学校缩写
        :param system: 需要爬取的系统：Jw 教务系统， Lib 图书馆
        :return: 如果不存在该配置，返回None；存在则返回对应的配置类。
        """

        #: 类名约定： 学校缩写 + 系统缩写 + Config
        #: 比如： 我们要获取南邮的教务系统的爬虫配置
        #: 类名为 NjuptJwConfig
        #: manyfaced.config中新增学校配置的命名需按照严格这个约定
        class_name = school + system + 'Config'

        config = __import__('manyfaced.config', globals(), locals(), [class_name], 0)
        try:
            config_class = config.__getattribute__(class_name)
        except AttributeError:
            return None
        return config_class

    def _get_captcha(self):
        pass

    def _decaptcha(self):
        pass

    def login(self, login_data):
        pass

    def fetch_data(self):
        pass

    def query_cache(self, student_id):
        pass

    def save_data(self, topic):
        pass

if __name__ == '__main__':
    b = BaseSpider('Njupt')

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/23
# @File Name: settings.py


import yaml


class Settings:
    def __init__(self):
        self.__setting_file = './bin/conf/config.yml'
        with open(self.__setting_file, encoding='utf-8') as fp:
            self.data = yaml.load(fp.read(), Loader=yaml.Loader)
        self.__servers = self.data['servers']
        self.__database = self.data['database']

    @property
    def host(self) -> str:
        """
        应用地址
        :return:
        """
        return self.__servers['host']

    @property
    def port(self) -> str:
        """
        应用端口
        :return:
        """
        return self.__servers['port']

    @property
    def type(self) -> str:
        """
        数据库类型
        :return:
        """
        return self.__database['type']

    @property
    def path(self) -> str:
        """
        数据库路径
        :return:
        """
        return self.__database['sqlite']['path']

    @property
    def name(self) -> str:
        """
        数据库名称
        :return:
        """
        return self.__database['sqlite']['path'].split('/')[-1]

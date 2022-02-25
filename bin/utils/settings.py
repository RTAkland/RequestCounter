#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/23
# @File Name: settings.py


import yaml
from typing import Dict


class Settings:
    def __init__(self):
        self.__setting_file = './bin/conf/config.yml'
        with open(self.__setting_file, encoding='utf-8') as fp:
            self.data = yaml.load(fp.read(), Loader=yaml.Loader)
        self.__servers = self.data['servers']
        self.__database = self.data['database']

    def all_data(self) -> Dict:
        """
        获取原始配置文件
        :return:
        """
        return self.data

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
        return self.__database['SQLite']['path']

    @property
    def name(self) -> str:
        """
        数据库名称
        :return:
        """
        return self.__database['SQLite']['path'].split('/')[-1]

    @property
    def mysql_host(self) -> str:
        """
        mysql数据库的地址
        :return: 
        """
        return self.__database['MySQL']['host']

    @property
    def mysql_port(self) -> int:
        """
        mysql数据库的端口
        默认3306
        :return:
        """
        return self.__database['MySQL']['port']

    @property
    def mysql_user(self) -> str:
        """
        mysql数据库的用户名
        :return:
        """
        return self.__database['MySQL']['user']

    @property
    def mysql_pwd(self) -> str:
        """
        mysql数据库的密码
        :return:
        """
        return self.__database['MySQL']['password']

    @property
    def mysql_db(self) -> str:
        """
        保存数据库数据库名
        :return:
        """
        return self.__database['MySQL']['db']

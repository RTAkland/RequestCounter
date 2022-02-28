#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/9
# @File Name: error.py


from typing import Optional
from flask import jsonify
from flask import Response
from bin.utils.logger import logger


class ErrorProcess:
    """处理错误的页面"""

    def __init__(self, db) -> None:
        """
        初始化
        :param db:
        """
        self.db = db  # 数据库对象
        self.response = {'code': Optional[int],
                         'msg': Optional[str],
                         'data': Optional[list]}

    def theme_error(self, theme: str) -> Response:
        """
        错误的主题
        :param theme:
        :return:
        """
        logger.debug('错误的主题')
        table_list = self.db().show_tables
        self.response['code'] = -2
        self.response['msg'] = f'错误的主题: {theme}. 以下是已保存的主题'
        self.response['data'] = table_list
        return jsonify(self.response)

    def length_error(self, length: int or str) -> Response:
        """
        数值太长显示此页面
        :param length:
        :return:
        """
        self.response['code'] = -2
        self.response['msg'] = f'错误的长度: {length}'
        self.response['data'] = []
        return jsonify(self.response)

    def count_error(self, name: str) -> Response:
        """
        数据过长重置数据
        :param name:
        :return:
        """
        self.db().update(name, 0)
        self.response['code'] = 200
        self.response['msg'] = '当前长度已超过最大可计数范围. 已将此名称的计数器重置为零'
        self.response['data'] = []
        return jsonify(self.response)

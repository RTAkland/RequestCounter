#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/9
# @File Name: error.py


from typing import Optional
from flask import jsonify
from flask import Response
from db.db import (update_data, fetch_table)


class ErrorProcess:
    """处理错误的页面"""
    def __init__(self):
        self.msg_template = {'code': -2,
                             'msg': '',
                             'data': Optional[list]}

    def get_theme_list(self) -> Response:
        """
        直接获取可选主题
        :return:
        """
        table_list = fetch_table()
        self.msg_template['code'] = 200
        self.msg_template['msg'] = '当前已保存到数据库的主题如下'
        self.msg_template['data'] = table_list
        return jsonify(self.msg_template)

    def error_theme(self, theme: str) -> Response:
        """
        错误的主题
        :param theme:
        :return:
        """
        table_list = fetch_table()
        self.msg_template['code'] = -2
        self.msg_template['msg'] = f'错误的主题: {theme}. 以下是已保存的主题'
        self.msg_template['data'] = table_list
        return jsonify(self.msg_template)

    def error_length(self, length: int) -> Response:
        """
        数值太长显示此页面
        :param length:
        :return:
        """
        self.msg_template['code'] = -2
        self.msg_template['msg'] = f'错误的长度: {length}'
        self.msg_template['data'] = None
        return jsonify(self.msg_template)

    def too_lang_to_count(self, name: str) -> Response:
        """
        数据过长重置数据
        :param name:
        :return:
        """
        update_data(name, 0)
        self.msg_template['code'] = 200
        self.msg_template['msg'] = '当前长度已超过最大可计数范围. 已将此名称的计数器重置为零'
        self.msg_template['data'] = None
        return jsonify(self.msg_template)

    def arg_not_be_full(self) -> Response:
        """
        参数不完整
        :return:
        """
        self.msg_template['code'] = -2
        self.msg_template['msg'] = '参数填写错误或填写不完整'
        self.msg_template['data'] = None
        return jsonify(self.msg_template)

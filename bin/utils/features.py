#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/28
# @File Name: features.py


from typing import Optional
from flask import jsonify
from flask import Response


class Features:
    """特殊操作"""

    def __init__(self, db) -> None:
        """
        初始化
        :param db:
        """
        self.db = db
        self.response = {'code': Optional[int],
                         'msg': Optional[str],
                         'data': Optional[list]}

    def theme_list(self) -> Response:
        """
        读取已有数据库并返回一个列表
        :return:
        """
        table_list = self.db().show_tables
        self.response['code'] = 200
        self.response['msg'] = '当前已保存到数据库的主题如下'
        self.response['data'] = table_list
        return jsonify(self.response)

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/9
# @File Name: errors.py

from . import api
from flask import jsonify


@api.errorhandler(404)
def page_not_found(e):
    return jsonify(
        {
            'code': 404,
            'msg': '页面未找到',
            'data': None
        }
    ), 404


@api.errorhandler(500)
def internal_server_error(e):
    return jsonify(
        {
            'code': 500,
            'msg': '服务器内部错误',
            'data': None
        }
    ), 500

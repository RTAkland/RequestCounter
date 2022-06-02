#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/9
# @File Name: __init__.py.py


from flask import Blueprint

api = Blueprint('api', __name__)

from . import views, errors

__all__ = [
    'api',
    'views',
    'errors'
]

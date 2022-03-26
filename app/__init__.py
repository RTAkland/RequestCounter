#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py


import os
import requests
from flask import Flask
from .main import main
from .db.db import SQLite


class Config:
    """基类配置"""
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False


def create_app():
    """创建主app"""
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config.from_object(Config)

    return app


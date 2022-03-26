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


def download():
    res = requests.get('http://resource-base.herokuapp.com/download/data.db')
    with open('./app/db/data.db', 'wb') as fp:
        fp.write(res.content)


if __name__ != '__main__':
    if not os.path.exists('./app/db/data.db'):
        print('数据库文件未找到, 正在下载中')
        download()
        print('下载完成')

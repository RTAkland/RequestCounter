#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py


import os
import requests
from flask import Flask
from config import config
from .main import main


def create_app(config_name):
    """创建主app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(main)

    return app


def download():
    res = requests.get('https://syncdatabase.herokuapp.com/sync/')
    with open('./app/db/data.db', 'wb') as fp:
        fp.write(res.content)


if __name__ == '__main__':
    if not os.path.exists('./app/db/data.db'):
        print('数据库文件未找到, 正在下载中')
        download()
        print('下载完成')

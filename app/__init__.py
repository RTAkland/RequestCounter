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


class Config:
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = './app/db/data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}


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

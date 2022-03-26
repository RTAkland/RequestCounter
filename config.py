#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/26
# @File Name: config.py


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

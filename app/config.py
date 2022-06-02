#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/5
# @File Name: config.py


import os
import logging
import platform
from logging.handlers import *


class Config:
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    SSL_REDIRECT = False
    SECRET_KEY = ''

    @staticmethod
    def init_app(app):
        if not os.path.exists('./app/logs'):
            os.mkdir('./app/logs')

        formatter = logging.Formatter(
            fmt='[%(asctime)s] |%(filename)s[%(funcName)s:%(lineno)d] |%(levelname)-8s |%(message)s',
            datefmt='%H:%M:%S')
        handler = logging.handlers.RotatingFileHandler(filename='./app/logs/access.log',
                                                       maxBytes=10240,
                                                       backupCount=10)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)

        if platform.system() == 'Linux':
            syslog_handler = SysLogHandler()
            syslog_handler.setLevel(logging.INFO)
            app.logger.addHandler(syslog_handler)

        app.logger.addHandler(handler)


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True


class ProfessionalConfig(ProductionConfig):
    SSL_REDIRECT = True


class VersionConfig:
    # 暂未开放/Not available
    version = ['v0.2.4']


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'professional': ProfessionalConfig,
    'heroku': HerokuConfig,

    'default': DevelopmentConfig
}

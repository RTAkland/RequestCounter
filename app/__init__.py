#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py


import os
import random
from flask import Flask
from flask_sslify import SSLify
from .main import main as main_blueprint
from .api import api as api_blueprint
from app.config import config


def generate_random_string(length):
    """
    生成随机密码
    :param length:
    :return:
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for _ in range(length))


def create_app(config_name):
    """
    创建 app
    :param config_name:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    if os.environ.get('SSL_REDIRECT'):
        SSLify(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1/')

    if not os.getenv('ACCESS_KEY'):
        access_key = generate_random_string(32)
        os.environ['ACCESS_KEY'] = access_key
    else:
        access_key = os.getenv('ACCESS_KEY')
    print('==========Access Key: {}=========='.format(access_key))

    return app


__all__ = [
    'db',
    'main',
    'tests',
    'utils',
    'create_app'
]

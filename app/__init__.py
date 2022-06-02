#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py


import os
from flask import Flask
from flask_sslify import SSLify
from .main import main as main_blueprint
from .api import api as api_blueprint
from .config import config
from .utils.password import generate_pwd


def create_app(config_name):
    """
    创建 app
    :param config_name:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    if app.config['SSL_REDIRECT']:
        SSLify(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1/')

    access_key = os.getenv('ACCESS_KEY')
    secret = app.config['SECRET_KEY']
    try:
        if not access_key and not secret:
            access_key = generate_pwd(16)
        elif not access_key and secret:
            access_key = secret
    finally:
        os.environ['ACCESS_KEY'] = access_key

    app.logger.info('访问密钥: {}'.format(access_key))

    return app


__all__ = [
    'db',
    'main',
    'tests',
    'utils',
    'create_app'
]

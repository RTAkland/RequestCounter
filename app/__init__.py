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
from .utils.logger import CreateLogger

logger = CreateLogger().get_logger()


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

    CreateLogger.init_app(app)

    if not os.getenv('ACCESS_KEY'):
        access_key = generate_pwd(32)
        os.environ['ACCESS_KEY'] = access_key
    else:
        access_key = os.getenv('ACCESS_KEY')

    logger.info('Access Key: {}'.format(access_key))

    return app


__all__ = [
    'db',
    'main',
    'tests',
    'utils',
    'logger',
    'create_app'
]

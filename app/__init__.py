#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py


from flask import Flask
from flask_sslify import SSLify
from .main import main
from app.config import config


def create_app(config_name):
    """创建主app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    sslify = SSLify(app)

    app.register_blueprint(main)

    return app


__all__ = [
    'db',
    'main',
    'tests',
    'utils',
    'create_app'
]

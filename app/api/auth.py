#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/5/2
# @File Name: auth.py


import os
from flask import request
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token):
    secret_key = os.getenv('ACCESS_KEY')
    key = request.args.get('key')
    if token or key == secret_key:
        return True
    elif (token == 'unittest' or
          key == 'unittest') and \
            'system' in request.path.split('/'):  # 限定在system这个接口使用unittest密钥获取数据
        return True
    return False

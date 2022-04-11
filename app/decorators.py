#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/11
# @File Name: decorators.py


import os
from flask import request
from flask import abort
from functools import wraps


def permission_required(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if request.args.get('key') != os.getenv('ACCESS_KEY'):
            abort(403)
        return func(*args, **kwargs)

    return decorated_func


#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/5
# @File Name: decorators.py

import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('数据库文件开始下载')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('下载结束, 耗时 {} 秒'.format(round(end - start, 2)))
        return result

    return wrapper




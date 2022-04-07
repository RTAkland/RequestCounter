#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py.py


import os
import sys
import requests
from ..decorators import time_it


@time_it
def download():
    res = requests.get('https://filebase.vercel.app/download/data.db')
    with open('./app/db/data.sqlite', 'wb') as fp:
        fp.write(res.content)


if not os.path.exists('./app/db/data.sqlite'):
    print('C: 数据库文件未找到, 正在下载中')
    try:
        download()
    except Exception as error:
        print('C: 下载失败, 错误原因:', error)
        print('I: 请手动下载数据库文件到 ./app/db/data.sqlite')
        sys.exit(1)

__all__ = [
    'db'
]

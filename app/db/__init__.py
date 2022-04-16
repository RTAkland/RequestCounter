#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py.py


import os
import sys
import requests


def download():
    res = requests.get('https://filebase.vercel.app/download/data.sqlite')
    with open('./app/db/data.sqlite', 'wb') as fp:
        fp.write(res.content)


if not os.path.exists('./app/db/data.sqlite'):
    try:
        download()
    except requests.exceptions as error:
        sys.exit(1)

__all__ = [
    'db'
]

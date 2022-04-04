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
    res = requests.get('https://markusjoe.github.io/static_file_hosting/data.sqlite')
    with open('./app/db/data.sqlite', 'wb') as fp:
        fp.write(res.content)


if __name__ != '__main__':
    if not os.path.exists('./app/db/data.sqlite'):
        print('数据库文件未找到, 正在下载中')
        try:
            download()
            print('下载完成')
        except Exception as error:
            print('下载失败, 错误原因:', error)
            print('请手动下载数据库文件到 ./app/db/data.sqlite')
            sys.exit(1)

__all__ = ['db']

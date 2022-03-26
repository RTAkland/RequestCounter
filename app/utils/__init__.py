#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py.py


import os
import requests


def download():
    res = requests.get('http://resource-base.herokuapp.com/download/data.db')
    with open('./app/db/data.db', 'wb') as fp:
        fp.write(res.content)


if __name__ == '__main__':
    if not os.path.exists('./app/db/data.db'):
        print('数据库文件未找到, 正在下载中')
        download()
        print('下载完成')

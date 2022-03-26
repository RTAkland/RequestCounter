#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: manage.py


import os
import requests
from gevent import pywsgi
from app import create_app

app = create_app()


def download():
    res = requests.get('http://resource-base.herokuapp.com/download/data.db')
    with open('./app/db/data.db', 'wb') as fp:
        fp.write(res.content)


if not os.path.exists('./app/db/data.db'):
    print('数据库文件未找到, 正在下载中')
    download()
    print('下载完成')

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()

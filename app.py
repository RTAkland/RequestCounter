#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: app.py


import time
from gevent import pywsgi
from flask import Flask
from flask import request
from flask import Response
from flask import make_response
from flask import send_from_directory
from bin.core.render_ import render_temp_
from bin.core.b64img import re_sort_number_image
from bin.core.length import make_html
from db.db import (fetch_data, update_data)

app = Flask(__name__)


def error_length(length: int) -> Response:
    """
    数值太长显示此页面
    :param length:
    :return:
    """
    response = make_response({'code': 200,
                              'message': f'错误的长度: {length}'})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def too_lang_to_count(name: str) -> Response:
    """
    数据过长重置数据
    :param name:
    :return:
    """
    update_data(name, 0)
    response = make_response({'code': 200,
                              'message': f'当前长度超过了最大可计数长度:10. 已将重置该名称的计数器'})
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def arg_not_be_full() -> Response:
    """
    参数不完整
    :return:
    """
    response = make_response({'code': 200,
                              'message': '参数填写不完整或填写错误'})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def build_page(name: str, length: int) -> list[Response] | list[bool | str] | list[bool]:
    """
    渲染最终的页面
    :param name:
    :param length:
    :return:
    """
    count = fetch_data(name)
    if len(str(count)) > length:
        return [False, too_lang_to_count(name)]
    if 7 <= length <= 10:
        make_html(length)
        zero_count = '0' * (length - len(str(count))) + str(count)
        sorted_image = re_sort_number_image(zero_count)
        return [True, render_temp_(length, name, sorted_image)]
    else:
        return [False, 'BadLength']


@app.route('/API', methods=['GET', 'POST'])  # 允许 GET 和 POST 方法
def api_page() -> Response | str:
    """
    API 页面函数
    :return:
    """
    if 'length' in request.args:
        try:
            length = int(request.args['length'])
        except ValueError:
            return arg_not_be_full()
    else:
        length = 8
    if 'name' in request.args:
        name = request.args['name']
        if name != '':  # 数据为空返回参数不完整界面
            resp = build_page(name, length)
            if resp[0]:
                response = make_response(resp[1])
                response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
                response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
                response.headers['date'] = time.ctime()
                return response
            elif resp[1] == 'BadLength':
                return error_length(length)
            else:
                return resp[1]
        else:
            return arg_not_be_full()
    else:
        return arg_not_be_full()


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    索引页面
    :return:
    """
    return send_from_directory('./static', 'index.html')


if __name__ == '__main__':
    # app.run(threaded=True)
    print('服务器已在http://127.0.0.1:5000 运行')
    try:
        server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
        server.serve_forever()
    except OSError:
        print('5000 端口被占用')


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
from db.db import (fetch_data,
                   update_data,
                   fetch_table)

app = Flask(__name__)


def get_theme_list() -> Response:
    """
    直接获取可选主题
    :return: 
    """
    table_list = fetch_table()
    response = make_response({'code': 200,
                              'msg': '可用主题如下',
                              'themes': table_list})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json: charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def error_theme(theme: str) -> Response:
    """
    错误的主题
    :param theme:
    :return:
    """
    table_list = fetch_table()
    response = make_response({'code': -2,
                              'msg': f'数据库内没有选择的主题: {theme}. 可用主题如下',
                              'themes': table_list})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def error_length(length: int) -> Response:
    """
    数值太长显示此页面
    :param length:
    :return:
    """
    response = make_response({'code': -2,
                              'msg': f'错误的长度: {length}'})
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
    response = make_response({'code': -2,
                              'msg': '当前长度超过了最大可计数长度:10. 已将重置该名称的计数器'})
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def arg_not_be_full() -> Response:
    """
    参数不完整
    :return:
    """
    response = make_response({'code': -2,
                              'msg': '参数填写不完整或填写错误'})
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
    response.headers['date'] = time.ctime()
    return response


def build_page(name: str, length: int, theme: str) -> list[bool | Response] | list[bool | str] | bool:
    """
    渲染最终的页面
    :param theme:
    :param name:
    :param length:
    :return:
    """
    count = fetch_data(name)
    if len(str(count)) > length:
        return [False, too_lang_to_count(name)]
    if 7 <= length <= 10:
        zero_count = '0' * (length - len(str(count))) + str(count)
        status, sorted_image, width, height = re_sort_number_image(zero_count, theme)
        if status:
            return [True, render_temp_(length, name, sorted_image, width, height)]
        else:
            return [False, 'BadTheme']
    else:
        return [False, 'BadLength']


@app.route('/get', methods=['GET', 'POST'])  # 允许 GET 和 POST 方法
def api_page() -> Response | str:
    """
    API 页面函数
    :return:
    """
    args = request.args
    name = str(args.get('name')).replace('None', 'null')
    length = args.get('length')
    theme = args.get('theme')
    if theme == 'ls':
        return get_theme_list()
    if name and name != 'null':
        if not length:
            length = 7
        else:
            length = int(length)
        if not theme:
            theme = 'moebooru'
        build_page_result = build_page(name, length, theme)
        if build_page_result[0]:
            response = make_response(build_page_result[1])
            response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
            response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
            response.headers['date'] = time.ctime()
            return response
        elif build_page_result[1] == 'BadLength':
            return error_length(length)
        elif build_page_result[1] == 'BadTheme':
            return error_theme(theme)
        else:
            return build_page_result[1]
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
    print('服务器已在 http://127.0.0.1:5000 运行')
    try:
        server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
        server.serve_forever()
    except OSError:
        print('5000 端口被占用')

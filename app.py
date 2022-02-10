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
from bin.core.error import ErrorProcess
from bin.core.render_ import render_temp_
from bin.core.b64img import re_sort_number_image
from db.db import fetch_data

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # 设置JSON消息不根据字母顺序重新排序
app.config['JSON_AS_ASCII'] = False  # 设置JSON消息显示中文


def build_page(name: str, length: int, theme: str) -> list[bool or Response] or list[bool or str] or bool:
    """
    渲染最终的页面
    :param theme:
    :param name:
    :param length:
    :return:
    """
    count = fetch_data(name)
    if len(str(count)) > length:
        return [False, ErrorProcess().too_lang_to_count(name)]
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
def api_page() -> Response or str:
    """
    API 页面函数
    :return:
    """
    args = request.args
    name = str(args.get('name')).replace('None', 'null')
    length = args.get('length')
    theme = args.get('theme')
    if theme == 'ls':
        return ErrorProcess().get_theme_list()
    if name and name != 'null':
        if not length:
            length = 7
        else:
            length = int(length)
        if not theme:
            theme = 'lewd'
        build_page_result = build_page(name, length, theme)
        if build_page_result[0]:
            response = make_response(build_page_result[1])
            response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
            response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
            response.headers['date'] = time.ctime()
            return response
        elif build_page_result[1] == 'BadLength':
            return ErrorProcess().error_length(length)
        elif build_page_result[1] == 'BadTheme':
            return ErrorProcess().error_theme(theme)
        else:
            return build_page_result[1]
    else:
        return ErrorProcess().arg_not_be_full()


@app.route('/', methods=['GET', 'POST'])
def index() -> Response:
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

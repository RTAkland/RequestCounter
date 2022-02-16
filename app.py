#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: app.py


import time
from flask import Flask
from flask import Response
from flask import jsonify
from flask import make_response
from flask import request
from gevent import pywsgi
from bin.utils.b64img import re_sort_number_image
from bin.utils.error import ErrorProcess
from bin.utils.render_ import render_temp_
from bin.utils.logger import logger
from db.sqlite import fetch_data

app = Flask(__name__, static_url_path='')
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
    if len(str(count)) > length:  # 判断在数据库内的长度是否超过了设定的(或预设的)长度
        return [False, ErrorProcess().too_lang_to_count(name)]
    if 7 <= length <= 10:  # 判断设定的长度是否超过阈值
        zero_count = '0' * (length - len(str(count))) + str(count)
        status, sorted_image, width, height = re_sort_number_image(zero_count, theme)
        if status:
            return [True, render_temp_(length, name, sorted_image, width, height)]
        else:
            return [False, 'BadTheme']
    else:
        return [False, 'BadLength']


@app.errorhandler(404)
def miss(reason) -> Response:
    """
    404页面使用json格式显示
    :param reason:
    :return:
    """
    return jsonify({'code': 404, 'msg': '没有定义的页面', 'data': None})


@app.errorhandler(500)
def error(reason) -> Response:
    """
    500 页面使用json格式显示
    :param reason:
    :return:
    """
    return jsonify({'code': 500, 'msg': '服务器内部错误', 'data': None})


@app.route('/get', methods=['GET', 'POST'])  # 允许 GET 和 POST 方法
def main() -> Response or str:
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
        elif type(length) is not int:
            return ErrorProcess().error_length(length)
        else:
            length = int(length)  # 将类型转换为整型
        if not theme:
            theme = 'lewd'
        build_page_result = build_page(name, length, theme)  # 开始处理整体页面
        if build_page_result[0]:
            response = make_response(build_page_result[1])  # 设置响应体 和 响应头
            response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
            # 防止浏览器和markdown编辑器缓存图片
            response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
            response.headers['date'] = time.ctime()
            return response
        elif build_page_result[1] == 'BadLength':  # 输入的长度错误
            return ErrorProcess().error_length(length)
        elif build_page_result[1] == 'BadTheme':  # 输入的主题错误
            return ErrorProcess().error_theme(theme)
        else:  # 长度过长无法计数重置数据库内的已有数据
            return build_page_result[1]
    else:
        return ErrorProcess().arg_not_be_full()


@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon() -> Response:
    """
    主页图标
    :return:
    """
    return app.send_static_file('favicon.ico')


@app.route('/', methods=['GET', 'POST'])
def index() -> Response:
    """
    索引页面
    :return:
    """
    return app.send_static_file('index.html')


@app.route('/arg')
def arg():
    import sys
    return {'data': sys.argv}


if __name__ == '__main__':
    # logger.info('服务器已在 http://127.0.0.1:5000 运行')
    # try:
    #     server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    #     server.serve_forever()
    # except OSError:
    #     logger.error('5000 端口被占用')
    # except KeyboardInterrupt:
    #     logger.info('程序已退出')

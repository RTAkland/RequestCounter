#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: app.py


import os
import time
from typing import Any
from flask import Flask
from flask import Response
from flask import jsonify
from flask import make_response
from flask import request
from flask import send_from_directory
from gevent import pywsgi
from bin.utils.error import ErrorProcess
from bin.utils.view import view_template
from bin.utils.logger import logger
from bin.utils.packing_logs import make_targz
from bin.utils.settings import Settings
from bin.db.sqlite import Database

app = Flask(__name__, static_url_path='')
app.config['JSON_SORT_KEYS'] = False  # 设置JSON消息不根据字母顺序重新排序
app.config['JSON_AS_ASCII'] = False  # 设置JSON消息显示中文


def build_page(name: str, length: int, theme: str) -> list[bool or Response] or list[bool or Any] or list[bool or str]:
    """
    渲染最终的页面
    :param theme:
    :param name:
    :param length:
    :return:
    """
    count = Database().fetch_data(name)
    if len(str(count)) > length:  # 判断在数据库内的长度是否超过了设定的(或预设的)长度
        return [False, ErrorProcess().too_lang_to_count(name)]
    if 7 <= length <= 10:  # 判断设定的长度是否超过阈值
        zero_count = '0' * (length - len(str(count))) + str(count)
        status, template = view_template(theme, length, name, zero_count)
        if status is True:
            return [True, template]
        else:
            return [False, 'BadTheme']
    else:
        return [False, 'BadLength']


@app.before_request
def requests_log() -> None:
    """
    向日志文件内请求记录
    :return:
    """
    if request.path != '/favicon.ico':  # 不记录favicon.ico的请求记录
        logger.info(f'{request.host} {request.method} {request.full_path}')

    file_list = os.listdir('./static/cache')
    file_list.remove('.gitkeep')
    for i in file_list:
        os.remove(f'./static/cache/{i}')

    origin_log_list = os.listdir('./bin/log')
    origin_log_list.remove('.gitkeep')
    if len(origin_log_list) > 100:
        for d in origin_log_list:
            try:
                os.remove(f'./bin/log/{d}')
            except PermissionError:
                pass


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


@app.route('/extra/db')
def export_db():
    """
    导出数据库
    :return:
    """
    dir_path = os.path.join(app.root_path, 'bin/db')
    return send_from_directory(dir_path, 'count.db', as_attachment=True)


@app.route('/extra/log', methods=['GET', 'POST'])
def view_log() -> Response:
    """
    下载日志
    :return:
    """
    make_targz()  # 打包tar.gz 文件
    log_file = f'{time.strftime("%Y-%m-%d %H")}.tar.gz'
    logger.warning(f'{request.host} {request.method} {request.path} -> Packed log files: {log_file}')
    dir_path = os.path.join(app.root_path, 'static/cache')
    return send_from_directory(dir_path, log_file, as_attachment=True)


@app.route('/get', methods=['GET', 'POST'])  # 允许 GET 和 POST 方法
def main() -> Response or str:
    """
    API 页面函数
    :return:
    """
    args = request.args
    name = str(args.get('name')).replace('None', 'null')
    theme = args.get('theme')
    length = str(args.get('length')).replace('None', '7')
    try:
        length = int(length)
    except ValueError:
        return ErrorProcess().error_length(length)
    if theme == 'ls':
        return ErrorProcess().get_theme_list()
    if name and name != 'null':
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
            logger.critical(f'用户: {name} 数据已被重置')
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


if __name__ == '__main__':
    conf = Settings()
    logger.info(f'服务器已在 http://127.0.0.1:{conf.port} 运行')
    try:
        server = pywsgi.WSGIServer((conf.host, conf.port), app, log=None)  # log=None 关闭日志输出, 使用自写的日志器记录
        server.serve_forever()
    except OSError:
        logger.error(f'{conf.port} 端口被占用')
    except KeyboardInterrupt:
        logger.info('程序已退出')

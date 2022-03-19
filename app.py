#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: app.py


from gevent import pywsgi
from flask import Flask
from flask import Response
from flask import request
from flask import make_response
from flask import render_template
from bin.utils.logger import logger
from bin.utils.features import Features
from bin.utils.settings import Settings
from bin.utils.error import ErrorProcess
from bin.utils.view import view_template

conf = Settings()

if conf.type.lower() == 'mysql':
    from bin.db.db import MySQL as db
else:
    from bin.db.db import SQLite as db

app = Flask(__name__, static_url_path='')
app.config['JSON_SORT_KEYS'] = False  # 设置JSON消息不根据字母顺序重新排序
app.config['JSON_AS_ASCII'] = False  # 设置JSON消息显示中文


@app.before_request
def requests_log() -> None:
    """
    向日志文件内请求记录
    :return:
    """
    if request.path != '/favicon.ico':  # 不记录favicon.ico的请求记录
        logger.info(f'{request.remote_addr} {request.method} {request.base_url}')


@app.route('/count/<string:name>', methods=['GET', 'POST'])  # 允许 GET 和 POST 方法
def main(name: str) -> Response or str:
    """
    API 页面函数
    :return:
    """
    args = request.args
    theme = args.get('theme', type=str)
    length = args.get('length', type=int)
    if not bool(theme):  # 判断主题是否存在查询参数内如果不存在则使用配置文件内的默认主题
        theme = conf.default_style
    elif theme == 'ls':
        return Features(db).theme_list()
    if not bool(length):
        length = 7
    if not db().exists_name(name):
        db().insert(name)
    count = db().fetch(name)
    if not db().exists_table(theme):
        return ErrorProcess(db).theme_error(theme)
    if 7 <= int(length) <= 10:  # 限定自定义长度阈值
        view_number = '0' * (int(length) - len(str(count[1]))) + str(count[1])
        response = make_response(view_template(theme, int(length), name, view_number, db))  # 设置响应体 和 响应头
        response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
        response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
        return response
    else:
        return ErrorProcess(db).length_error(length)


@app.route('/', methods=['GET', 'POST'])
def home() -> str:
    """
    主页面
    :return:
    """
    return render_template('index.html', remote_address=request.remote_addr)


if __name__ == '__main__':
    logger.info(f'服务器已在 http://127.0.0.1:{conf.port} 运行')
    try:
        server = pywsgi.WSGIServer((conf.host, conf.port), app, log=None)  # log=None 关闭日志输出, 使用自写的日志器记录
        server.serve_forever()
    except OSError:
        logger.critical(f'{conf.port} 端口被占用 已退出')
    except KeyboardInterrupt:
        logger.info('程序已退出')

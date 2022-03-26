#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: views.py


from flask import abort
from flask import jsonify
from flask import request
from flask import Response
from flask import make_response
from flask import render_template
from . import main
from ..db.db import SQLite as db
from ..utils.view import view


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    主页
    :return:
    """
    return render_template('index.html', remote_address=request.remote_addr)


@main.route('/api/v1/<string:name>', methods=['GET', 'POST'])
@main.route('/count/<string:name>', methods=['GET', 'POST'])
def api_v1(name: str):
    length = request.args.get('length', type=int)
    theme = request.args.get('theme', type=str)
    if not bool(length):
        length = 7
    if not bool(theme):
        theme = 'lewd'
    if not db().exists_name(name):
        db().insert(name)
    if not db().exists_table(theme):
        abort(500)
    if 7 <= length <= 10:
        data = db().fetch(name)
        number = '0' * (length - len(str(data[-1]))) + str(data[-1])
        # 将设置的长度减去数据库内已有的数据库字符串长度剩下的结果为[0]的个数
        # 再将这个字符串后拼接上数据库内已有次数的字符串, 就可以得到最终的结果
        response = make_response(view(theme, int(length), name, number))
        response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
        response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
        return response
    return abort(500)


@main.route('/exists-table', methods=['GET', 'POST'])
@main.route('/exists', methods=['GET', 'POST'])
def show_tables() -> Response:
    """
    返回已有表
    :return:
    """
    tables = db().show_tables
    return jsonify({'code': 200, 'msg': '已有表', 'data': [tables]})

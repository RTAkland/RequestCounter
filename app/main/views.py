#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: views.py


from flask import abort
from flask import request
from flask import make_response
from flask import render_template
from ..db.db import SQLite as db
from ..utils.response import index_
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    主页
    :return:
    """
    return render_template('index.html', remote_address=request.remote_addr)


@main.route('/count/<string:name>', methods=['GET', 'POST'])
def home(name: str):
    """
    主视图
    :param name:
    :return:
    """
    length = request.args.get('length', 7, type=int)
    theme = request.args.get('theme', 'lewd', type=str)
    if not db().exists_name(name):
        db().insert(name)
    if not db().exists_table(theme):
        abort(500)
    if 7 <= length <= 10:
        data = db().fetch(name)
        if len(str(data[1])) >= 10:  # 计数的数据长度超过最大位数将次数设为1
            db().update(name, 0)
        # 使用设置的长度减去已有数据的长度, 将结果转换为string类型, 再和数据库内的数据进行拼接
        number = '0' * (length - len(str(data[-1]))) + str(data[-1])
        response = make_response(index_(theme, int(length), name, number))
        response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
        response.headers['cache-control'] = 'max-age=0, no-cache, no-store, must-revalidate'
        return response
    return abort(500)

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/9
# @File Name: views.py


import os
from functools import wraps
from flask import abort
from flask import jsonify
from flask import request
from flask import send_file
from ..db.db import SQLite as db
from . import api


def permission_required(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if request.args.get('key') != os.getenv('ACCESS_KEY'):
            abort(403)
        return func(*args, **kwargs)

    return decorated_func


@api.route('/overall/', methods=['GET', 'POST'])
@permission_required
def overall():
    """
    查询ReqCount表内所有的源数据
    :return:
    """
    limit = request.args.get('limit', type=int)
    try:
        data = db().exec('select * from reqcount;')
        format_data = []
        for i in data:
            format_data.append({'name': i[0], 'times': i[1]})
        return jsonify(
            {
                'code': 200,
                'msg': 'Success. Total: %s row(s)' % len(data),
                'data': format_data[:limit]
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'code': -200,
                'msg': 'Error',
                'data': e
            }
        ), 500


@api.route('/query/', methods=['GET', 'POST'])
@permission_required
def query():
    """
    查询指定名称的计数数据
    :return:
    """
    name = request.args.get('name', type=str)
    nochange = request.args.get('nochange', type=bool)
    if nochange:
        nochange = True
    if not db().exists_name(name):
        return jsonify(
            {
                'code': -200,
                'msg': 'Failed. No such name',
                'data': None
            }
        ), 404
    else:
        data = db().fetch(name, nochange)
        return jsonify(
            {
                'code': 200,
                'msg': 'Success',
                'data': data
            }
        ), 200


@api.route('/theme/', methods=['GET', 'POST'])
@permission_required
def theme():
    """
    查询数据库内主题的源数据
    :return:
    """
    _theme = request.args.get('name', type=str)
    if not db().exists_table(_theme):
        return jsonify(
            {
                'code': 404,
                'msg': 'Failed. No such theme',
                'data': None
            }
        ), 404
    else:
        data = db().fetching_table(_theme)
        return jsonify(
            {
                'code': 200,
                'msg': 'Success',
                'data': data
            }
        ), 200


@api.route('/alltables/', methods=['GET', 'POST'])
@permission_required
def all_tables():
    """
    查询所有已有表
    :return:
    """
    data = db().show_tables
    return jsonify(
        {
            'code': 200,
            'msg': 'Success',
            'data': data
        }
    ), 200


@api.route('/export/', methods=['GET', 'POST'])
@api.route('/export/<key>', methods=['GET', 'POST'])
@permission_required
def export(key: str = None):
    """
    导出数据库文件
    :return:
    """
    return send_file('./db/data.sqlite', as_attachment=True)

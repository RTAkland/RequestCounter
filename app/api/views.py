#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/9
# @File Name: views.py


from flask import jsonify
from flask import request
from flask import send_file
from ..db.db import SQLite as db
from ..decorators import permission_required
from . import api


@api.route('/overall/', methods=['GET', 'POST'])
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
@permission_required
def export():
    """
    导出数据库文件
    :return:
    """
    return send_file('./db/data.sqlite', as_attachment=True)


@api.route('/test', methods=['GET', 'POST'])
def test_api():
    """
    测试专用接口
    :return:
    """
    data = db().fetch('test-example')
    return str(data[1])

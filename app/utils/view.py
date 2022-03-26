#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: view.py


from ..db.db import SQLite as db
from flask import request
from flask import render_template
from typing import Tuple


def view(theme: str,
         length: int,
         name: str,
         count: str
         ) -> str or Tuple[bool, str]:
    """
    渲染模板
    :param theme:
    :param length:
    :param name:
    :param count:
    :return:
    """
    datas = db().fetching_table(theme)
    context = []
    for i in count:
        if i == '0':
            context.append({'base64': datas[0]['base64'],
                            'width': datas[0]['width'],
                            'height': datas[0]['height']})
        elif i == '1':
            context.append({'base64': datas[1]['base64'],
                            'width': datas[1]['width'],
                            'height': datas[1]['height']})
        elif i == '2':
            context.append({'base64': datas[2]['base64'],
                            'width': datas[2]['width'],
                            'height': datas[2]['height']})
        elif i == '3':
            context.append({'base64': datas[3]['base64'],
                            'width': datas[3]['width'],
                            'height': datas[3]['height']})
        elif i == '4':
            context.append({'base64': datas[4]['base64'],
                            'width': datas[4]['width'],
                            'height': datas[4]['height']})
        elif i == '5':
            context.append({'base64': datas[5]['base64'],
                            'width': datas[5]['width'],
                            'height': datas[5]['height']})
        elif i == '6':
            context.append({'base64': datas[6]['base64'],
                            'width': datas[6]['width'],
                            'height': datas[6]['height']})
        elif i == '7':
            context.append({'base64': datas[7]['base64'],
                            'width': datas[7]['width'],
                            'height': datas[7]['height']})
        elif i == '8':
            context.append({'base64': datas[8]['base64'],
                            'width': datas[8]['width'],
                            'height': datas[8]['height']})
        elif i == '9':
            context.append({'base64': datas[9]['base64'],
                            'width': datas[9]['width'],
                            'height': datas[9]['height']})

    for p, i in zip(context, range(0, length)):
        p['position'] = i * p['width']  # 设置每张图片对应的位置

    general_width = datas[0]['width'] * length  # 计算出图片总长度
    general_height = datas[0]['height']  # 总宽度

    return render_template('view.html',
                           context=context,
                           title=name,
                           address=request.remote_addr,
                           general_height=general_height,
                           general_width=general_width)

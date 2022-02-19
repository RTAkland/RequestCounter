#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/18
# @File Name: view.py


from flask import render_template
from bin.db.sqlite import fetch_style_data
from bin.db.sqlite import fetch_table


def view_template(style: str, length: int, name: str, count: str) -> str or tuple[bool, str]:
    """
    渲染模板
    :param count: 
    :param name:
    :param length:
    :param style:
    :return:
    """
    if style not in fetch_table():
        return [False, 'BadLength']
    origin_data = fetch_style_data(style)  # 获取数据库内的文件
    context = []
    if count != '0000000000':
        for i in count:  # 通过elif语句依次判断数字
            if i == '0':
                context.append({'base64': origin_data[0]['base64'],
                                'width': origin_data[0]['width'],
                                'height': origin_data[0]['height']})
            elif i == '1':
                context.append({'base64': origin_data[1]['base64'],
                                'width': origin_data[1]['width'],
                                'height': origin_data[1]['height']})
            elif i == '2':
                context.append({'base64': origin_data[2]['base64'],
                                'width': origin_data[2]['width'],
                                'height': origin_data[2]['height']})
            elif i == '3':
                context.append({'base64': origin_data[3]['base64'],
                                'width': origin_data[3]['width'],
                                'height': origin_data[3]['height']})
            elif i == '4':
                context.append({'base64': origin_data[4]['base64'],
                                'width': origin_data[4]['width'],
                                'height': origin_data[4]['height']})
            elif i == '5':
                context.append({'base64': origin_data[5]['base64'],
                                'width': origin_data[5]['width'],
                                'height': origin_data[5]['height']})
            elif i == '6':
                context.append({'base64': origin_data[6]['base64'],
                                'width': origin_data[6]['width'],
                                'height': origin_data[6]['height']})
            elif i == '7':
                context.append({'base64': origin_data[7]['base64'],
                                'width': origin_data[7]['width'],
                                'height': origin_data[7]['height']})
            elif i == '8':
                context.append({'base64': origin_data[8]['base64'],
                                'width': origin_data[8]['width'],
                                'height': origin_data[8]['height']})
            elif i == '9':
                context.append({'base64': origin_data[9]['base64'],
                                'width': origin_data[9]['width'],
                                'height': origin_data[9]['height']})

    for p, i in zip(context, range(0, length)):
        p['position'] = i * p['width']

    general_width = origin_data[0]['width'] * length
    general_height = origin_data[0]['height']

    return True, render_template('view.html',
                                 context=context,
                                 title=name,
                                 general_height=general_height,
                                 general_width=general_width)

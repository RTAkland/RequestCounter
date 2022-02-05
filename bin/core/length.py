#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/5
# @File Name: length.py


def make_html(length: int, svg_width: int = 45, svg_height: int = 70) -> None:
    """
    生成html
    :param svg_height:
    :param svg_width:
    :param length:
    :return:
    """

    html_head = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="%(w)s" height="%(h)s" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<title>{{ title }}</title>
<g>\n"""
    svg_tag = """   <image x="%(x)s" y="0" width="%(w)s" height="%(h)s" xlink:href="{{ svg_img_%(i)s }}"></image>\n"""
    html_feet = """</g></svg>"""
    html_head = html_head % {'w': length * svg_width, 'h': svg_height}  # 总体宽度
    for i in range(length):  # 拼接出完整的html
        html_head += svg_tag % {'x': i * svg_width, 'w': svg_width, 'h': svg_height, 'i': i}
    html_head += html_feet  # 加上结尾标签
    with open('./templates/index.html', 'w', encoding='utf-8') as template_fp:  # 写入文件
        template_fp.write(html_head)

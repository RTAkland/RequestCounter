#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: b64img.py


import sqlite3
from typing import Any
from db.db import fetch_table


def re_sort_number_image(origin_number: str, theme: str) -> tuple[bool, bool, bool, bool] or list[
    bool or list[Any] or Any]:
    """
    返回一个排列好的svg base64代码列表
    :param theme:
    :param origin_number:
    :return:
    """

    table_list = fetch_table()
    if theme not in table_list:
        return False, False, False, False

    width_list = []
    height_list = []
    b_64_list = []
    cursor.execute('select * from %(name)s' % {'name': theme})
    data = cursor.fetchall()
    for i in data:
        width_list.append(i[2])
        height_list.append(i[3])
        b_64_list.append(i[1])

    final_b64_img_code = []
    if origin_number != '0000000000':
        for i in origin_number:
            if i == '0':
                final_b64_img_code.append(b_64_list[0])
            elif i == '1':
                final_b64_img_code.append(b_64_list[1])
            elif i == '2':
                final_b64_img_code.append(b_64_list[2])
            elif i == '3':
                final_b64_img_code.append(b_64_list[3])
            elif i == '4':
                final_b64_img_code.append(b_64_list[4])
            elif i == '5':
                final_b64_img_code.append(b_64_list[5])
            elif i == '6':
                final_b64_img_code.append(b_64_list[6])
            elif i == '7':
                final_b64_img_code.append(b_64_list[7])
            elif i == '8':
                final_b64_img_code.append(b_64_list[8])
            elif i == '9':
                final_b64_img_code.append(b_64_list[9])

        return [True, final_b64_img_code, width_list[0], height_list[0]]
    else:
        for i in range(10):
            final_b64_img_code.append(b_64_list[0])
        return [True, final_b64_img_code, width_list[0], height_list[0]]


if __name__ != '__main__':
    conn = sqlite3.connect('./bin/assets/theme.db', check_same_thread=False)
    cursor = conn.cursor()

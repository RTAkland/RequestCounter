#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: b64img.py


import sqlite3


def re_sort_number_image(origin_number: str, theme: str) -> list:
    """
    返回一个排列好的svg base64代码列表
    :param theme:
    :param origin_number:
    :return:
    """
    print(theme)
    if theme == 't1':
        cursor.execute('select * from theme1')
    elif theme == 't2':
        cursor.execute('select * from theme2')
    elif theme == 'gelbooru':
        cursor.execute('select * from gelbooru')
    elif theme == 'gelbooru-h':
        cursor.execute('select * from gelbooruh')
    elif theme == 'moebooru':
        cursor.execute('select * from moebooru')
    elif theme == 'moebooru-h':
        cursor.execute('select * from moebooruh')
    elif theme == 'rule34':
        cursor.execute('select * from rule34')
    else:
        cursor.execute('select * from rule34')
    data = cursor.fetchall()
    temp_dict = {}
    for k, v in data:
        temp_dict.setdefault(k, []).append(v)
    for i, c in zip(temp_dict.keys(), temp_dict.values()):
        temp_dict[i] = c[0]

    final_b64_img_code = []
    if origin_number != '0000000000':
        for i in origin_number:
            if i == '0':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '1':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '2':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '3':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '4':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '5':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '6':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '7':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '8':
                final_b64_img_code.append(temp_dict.get(str(i)))
            elif i == '9':
                final_b64_img_code.append(temp_dict.get(str(i)))

        return final_b64_img_code
    else:
        for i in range(10):
            final_b64_img_code.append(temp_dict.get(str(0)))
        return final_b64_img_code


if __name__ != '__main__':
    conn = sqlite3.connect('./bin/assets/theme.db')
    cursor = conn.cursor()

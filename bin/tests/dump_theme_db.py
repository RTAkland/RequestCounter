#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/7
# @File Name: dump_theme_db.py


import os
import base64
import sqlite3

conn = sqlite3.connect('../assets/theme.db')
cursor = conn.cursor()


dir_name = 'gelbooru-h'
file_list = os.listdir(f'../assets/themes/moe_theme/{dir_name}')
dict_count = 0
img_dict = {}
for i in file_list:
    with open(f'../assets/themes/moe_theme/{dir_name}/{i}', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = f'data:image/jpeg;base64,' + base64_data.decode('utf-8')
        img_dict[str(dict_count)] = base64_code
        dict_count += 1
for k, v in zip(img_dict.keys(), img_dict.values()):
    cursor.execute("insert into gelbooruh values(?, ?)", (k, v))
    conn.commit()

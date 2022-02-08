#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/8
# @File Name: insert_db.py


import os
import base64
from PIL import Image
import sqlite3

conn = sqlite3.connect('../theme.db')
cursor = conn.cursor()


def get_size(file):
    img = Image.open(file)
    return img.size


dir_name = './rfck'
lst = os.listdir(dir_name)
c = 0
for i in lst:
    w, h = get_size(f'{dir_name}/{i}')
    type_ = i.split('.')[-1]
    if type_ == 'png':
        type_ = 'jepg'
    else:
        type_ = 'gif'
    with open(f'./{dir_name}/{i}', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = f'data:image/{type_};base64,' + base64_data.decode('utf-8')
    cursor.execute('insert into rfck values(?, ?, ?, ?)', (c, base64_code, w, h))
    conn.commit()
    c += 1


#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/8
# @File Name: img_size.py

import os
from PIL import Image
import sqlite3


def get_info(path, file):
    for i in path:
        img = Image.open(f'../assets/themes/{path}/{file}')
        imgSize = img.size
        w = img.width
        h = img.height
        f = img.format
        print(imgSize)
        print(w, h, f)


file_list = os.listdir('../assets/themes/')
for p in file_list:
    lst = os.listdir(f'../assets/themes/{p}')
    for i in lst:
        get_info(p, i)



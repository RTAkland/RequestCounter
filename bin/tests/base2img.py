#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: base2img.py

import base64
import os


def convert_single() -> None:
    """
    
    :return: 
    """
    # image转base64
    with open(f'../../static/example.png', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = 'data:image/jpeg;base64,' + base64_data.decode('utf-8')
        print(base64_code)


def convert_multi() -> None:
    """

    :return:
    """
    file_list = os.listdir('../res/images')
    dict_count = 0
    img_dict = {}
    for i in file_list:
        with open(f'../res/images/theme2{i}', 'rb') as f:
            base64_data = base64.b64encode(f.read())
            base64_code = 'data:image/svg+xml;base64,' + base64_data.decode('utf-8')
            img_dict[str(dict_count)] = base64_code
            dict_count += 1

    print(img_dict)


convert_multi()
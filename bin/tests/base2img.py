#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: base2img.py

import base64


def convert() -> None:
    """
    
    :return: 
    """
    # image转base64
    with open(f'../../static/example.png', 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = 'data:image/jpeg;base64,' + base64_data.decode('utf-8')
        print(base64_code)


convert()

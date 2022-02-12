#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/12
# @File Name: img2base64.py


import base64

print(base64.b64encode(open('example.png', 'rb').read()).decode('utf-8'))
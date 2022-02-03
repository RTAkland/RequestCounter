#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: resp_test.py

import requests
import random

name_str = random.sample(range(1, 100), 30)
for i in name_str:
    resp = requests.get(f'http://127.0.0.1:8000/API?owner={i}')
    print(resp.content)
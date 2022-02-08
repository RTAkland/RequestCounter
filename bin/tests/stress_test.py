#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/7
# @File Name: stress_test.py


import requests


for i in range(100):
    print(requests.get('http://127.0.0.1:5000/API?name=89999&length=10&theme=t2').elapsed.microseconds)
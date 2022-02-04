#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: resp_test.py

import requests
import random


def request_test() -> None:
    """
    请求测试
    :return:
    """
    for i in range(100):
        resp = requests.get(f'http://127.0.0.1:8000/API?name={i}')
        print(resp)


def download_test() -> None:
    """
    下载测试
    :return:
    """

    resp = requests.get('https://count.getloli.com/get/@Moe-counter.github')
    with open('download_test.html', 'wb') as fp:
        fp.write(resp.content)


request_test()
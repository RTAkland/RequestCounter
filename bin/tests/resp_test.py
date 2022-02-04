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
    name_str = random.sample(range(1, 100), 30)
    for i in name_str:
        resp = requests.get(f'http://127.0.0.1:8000/API?owner={i}')
        print(resp.content)


def download_test() -> None:
    """
    下载测试
    :return:
    """

    resp = requests.get('https://count.getloli.com/get/@Moe-counter.github')
    with open('download_test.html', 'wb') as fp:
        fp.write(resp.content)


download_test()

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/8
# @File Name: download_img.py

import os
import requests
import threading

proxies = {
    'http': '127.0.0.1:8889',
    'https': '127.0.0.1:8889'
}


def thread_(i, main_url, dir):
    res = requests.get(f'{main_url}/{i}.gif', proxies=proxies)
    with open(f'../assets/themes/{dir}/{i}.gif', 'wb') as f:
        f.write(res.content)


while True:
    url = input('->')
    url = url.replace('https://', '|')
    url = ''.join(url.split('/')[:-2]).replace('|', 'https://') + '/counter'
    dir = url.split('.')[0].split('//')[-1]
    os.mkdir(f'../assets/themes/{dir}')
    for i in range(0, 10):
        threading.Thread(target=thread_, args=(i, url, dir)).start()

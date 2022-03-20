#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/17
# @File Name: __init__.py


import os
import time
import requests
from bin.utils.logger import logger


def cost(func):
    def wrapper(*args, **kwargs):
        logger.info('开始下载')
        s = time.time()
        execute = func(*args, **kwargs)
        e = time.time()
        logger.info(f'下载结束, 用时: {round(e - s, 2)} s')
        return execute

    return wrapper


@cost
def download(url: str) -> None:
    """
    单线程下载资源
    :param url:
    :return:
    """
    content = requests.get(url, timeout=10, stream=True).content
    with open('./bin/db/data.db', 'wb') as fp:
        fp.write(content)


if __name__ != '__main__':
    if not os.path.exists('./bin/db/data.db'):
        logger.warning('数据库文件不存在, 即将开始下载')
        try:
            download('https://resource-base.herokuapp.com/download/data.db')
        except requests.Timeout:
            logger.critical('连接超时')

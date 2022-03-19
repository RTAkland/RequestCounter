#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/17
# @File Name: __init__.py


import os
import sys
import time
import requests
import threading
from bin.utils.logger import logger


class MultiThreaded(threading.Thread):
    def __init__(self,
                 start_: int,
                 end_: int,
                 id_: int,
                 url: str,
                 name: str
                 ) -> None:
        """
        初始化类
        :param start_: 开始点
        :param end_: 结束点
        :param id_: 线程id
        :param url: 文件url
        :param name: 文件名
        """
        super(MultiThreaded, self).__init__()
        self.start_ = start_
        self.end_ = end_
        self.id = id_
        self.url = url
        self.name = name

    def download(self):
        """
        下载文件
        写入文件
        :return:
        """
        logger.info(f'线程: {self.id} 开始下载')
        res = requests.get(self.url, headers={'Range': f'Bytes={self.start_}-{self.end_}'}, timeout=10).content
        with open(self.name, 'r+b') as fp:
            fp.seek(self.start_)
            fp.write(res)
        logger.info(f'线程: {self.id} 结束下载')

    def run(self):
        """
        重写run()方法开始下载
        :return:
        """
        self.download()


def cost(func):
    def wrapper(*args, **kwargs):
        logger.info('文件开始开始下载')
        s = time.time()
        execute = func(*args, **kwargs)
        e = time.time()
        logger.info(f'下载结束, 用时: {round(e - s, 2)} s')
        return execute

    return wrapper


@cost
def main(url: str, name: str, path: str = '.', workers: int = 8):
    """
    主函数
    :param url:
    :param name:
    :param path:
    :param workers:
    :return:
    """
    logger.info(f'本次下载使用线程数: {workers}')
    file_size = int(requests.get(url, timeout=10).headers['Content-Length'])
    if requests.get(url, timeout=10).status_code == 302:
        url = requests.get(url).headers['Location']
        logger.warning(f'下载地址已重定向到了: {url}')
    logger.info(f'文件大小: {round(file_size / 1024 / 1024, 2)} Mb')
    offset = int(file_size / workers)
    start = 0
    open(path + name, 'wb').close()
    for i in range(workers):
        if i == workers - 1:
            end = file_size
        elif i != 0:
            end = i * offset
        else:
            end = offset
        threads = MultiThreaded(start, end, i, url, path + name)
        threads.start()
        threads.join()
        start = end + 1


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
            main('https://filebase.vercel.app/download/data.db', 'data.db', './bin/db/')
        except requests.Timeout:
            logger.critical('连接超时, 将使用单线程重新尝试下载')
            try:
                download('https://filebase.vercel.app/download/data.db')
            except requests.Timeout:
                logger.critical('连接超时, 请自行前往 https://filebase.vercel.app/download/data.db 下载文件')
                logger.critical('并放置在 ./bin/db/ 文件夹内')
                sys.exit(-1)

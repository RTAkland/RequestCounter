#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/17
# @File Name: __init__.py


import os
import requests
import threading
from bin.utils.logger import logger


class Threaded(threading.Thread):
    def __init__(self, s, e, fp, id_, url):
        """
        初始化类
        :param s: 开始点
        :param e: 结束点
        :param fp: 文件操作
        :param id_: 线程id
        :param url: 文件url
        """
        super().__init__()
        self.start_ = s
        self.end_ = e
        self.fp = fp
        self.id = id_
        self.url = url

    def download(self):
        """
        下载文件
        写入文件
        :return:
        """
        logger.info(f'线程: {self.id} 开始下载')
        res = requests.get(self.url, headers={'Range': f'Bytes={self.start_}-{self.end_}'}).content
        self.fp.seek(self.start_)
        self.fp.write(res)
        logger.info(f'线程: {self.id} 结束下载')

    def run(self):
        """
        重写run()方法开始下载
        :return:
        """
        self.download()


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
    file_size = int(requests.get(url).headers['Content-Length'])
    if requests.get(url).status_code == '302':
        url = requests.get(url).headers['Location']
        logger.warning(f'下载地址已重定向到了: {url}')
    logger.info(f'文件大小: {round(file_size / 1024 / 1024, 2)} Mb')
    offset = int(file_size / workers)
    start = 0
    open(path + name, 'wb').close()
    fp = open(path + name, 'r+b')
    for i in range(workers):
        if i == workers - 1:
            end = file_size
        elif i != 0:
            end = i * offset
        else:
            end = offset
        threads = Threaded(start, end, fp, i, url)
        threads.start()
        threads.join()
        start = end + 1


if __name__ != '__main__':
    if not os.path.exists('./bin/db/data.db'):
        logger.warning('数据库文件不存在, 即将开始下载')
        main('https://themedatabase.vercel.app/assets', 'data.db', './bin/db/', 6)

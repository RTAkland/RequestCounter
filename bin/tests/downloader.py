#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/2
# @File Name: downloader.py


import requests
import threading
from bin.utils.logger import logger


class Threaded(threading.Thread):
    def __init__(self, s, e, fp, id_, url):
        super().__init__()
        self.start_ = s
        self.end_ = e
        self.fp = fp
        self.id = id_
        self.url = url

    def download(self):
        logger.info(f'线程: {self.id} 开始下载')
        res = requests.get(self.url, headers={'Range': f'Bytes={self.start_}-{self.end_}'}).content
        self.fp.seek(self.start_)
        self.fp.write(res)
        logger.info(f'线程: {self.id} 结束下载')

    def run(self):
        self.download()


def main(url: str, path: str = '.', workers: int = 8):
    logger.info(f'本次下载使用线程数: {workers}')
    file_name = url.split('/')[-1]
    file_size = int(requests.get(url).headers['Content-Length'])
    if requests.get(url).status_code == '302':
        url = requests.get(url).headers['Location']
    offset = int(file_size / workers)
    start = 0
    open(path + file_name, 'wb').close()
    fp = open(path + file_name, 'r+b')
    for i in range(workers):
        if i == workers - 1:
            end = file_size
        elif i != 0:
            end = i * offset
        else:
            end = offset
        Threaded(start, end, fp, i, url).start()
        start = end + 1


if __name__ == '__main__':
    main('https://i0.hdslb.com/bfs/archive/cc013c0a726082e07772ec77d5c0444ac7d40a6f.jpg')

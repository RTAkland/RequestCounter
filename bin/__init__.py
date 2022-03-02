#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/17
# @File Name: __init__.py


import os
import sys
from requests import get
from threading import Lock
from bin.utils.logger import logger
from bin.utils.settings import Settings
from concurrent.futures import ThreadPoolExecutor, wait

lock = Lock()
conf = Settings()


class Downloader:
    def __init__(self, url, nums, file):
        """
        初始化
        :param url:
        :param nums:
        :param file:
        """
        self.url = url
        self.num = nums
        self.name = file
        r = get(self.url)
        self.size = int(r.headers['Content-Length'])
        logger.info('文件大小为：{} Mb'.format(round(self.size / 1024 / 1024, 2)))

    def down(self, start, end):
        """
        下载
        :param start:
        :param end:
        :return:
        """
        headers = {'Range': 'bytes={}-{}'.format(start, end)}
        r = get(self.url, headers=headers, stream=True)
        lock.acquire()
        with open(self.name, "rb+") as fp:
            fp.seek(start)
            fp.write(r.content)
            lock.release()

    def run(self):
        """
        运行
        :return:
        """
        fp = open(self.name, "wb")
        fp.truncate(self.size)
        fp.close()
        part = self.size // self.num
        pool = ThreadPoolExecutor(max_workers=self.num)
        futures = []
        for i in range(self.num):
            start = part * i
            if i == self.num - 1:
                end = self.size
            else:
                end = start + part - 1
            futures.append(pool.submit(self.down, start, end))
        wait(futures)
        logger.info('数据库: %s 下载完成' % self.name.split('/')[-1])


if __name__ != '__main__':
    if not os.path.exists('./bin/db/data.db'):
        logger.error('没有检测到数据库文件, 即将开始下载data.db')
        Downloader('https://themedatabase.vercel.app/assets', 4, './bin/db/data.db').run()

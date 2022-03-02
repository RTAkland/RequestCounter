#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/2
# @File Name: downloader.py


from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock
from requests import get
from bin.utils.logger import logger

lock = Lock()


class Downloader:
    def __init__(self, url, nums, file):
        self.url = url
        self.num = nums
        self.name = file
        r = get(self.url)
        self.size = int(r.headers['Content-Length'])
        logger.info('该文件大小为：{} bytes'.format(self.size))

    def down(self, start, end):
        headers = {'Range': 'bytes={}-{}'.format(start, end)}
        r = get(self.url, headers=headers, stream=True)
        lock.acquire()
        with open(self.name, "rb+") as fp:
            fp.seek(start)
            fp.write(r.content)
            lock.release()

    def run(self):
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
                logger.info('本线程下载范围: {}->{}'.format(start, end))
            futures.append(pool.submit(self.down, start, end))
        wait(futures)
        logger.info('%s 下载完成' % self.name)


ss = Downloader(
    'https://themedatabase.vercel.app/source/sql', 6, "origin.sql")
ss.run()

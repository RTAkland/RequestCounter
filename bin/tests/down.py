#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/4
# @File Name: down.py


import sys
import time
import requests
import threading


class Downloader(threading.Thread):
    """继承threading实现多线程"""

    def __init__(self, start_: int, end_: int, t_id: int, url: str, name: str):
        """
        初始化类
        :param start_: seek开始点
        :param end_: seek结束点
        :param t_id: 线程id
        :param url: 资源地址
        :param name: 文件名
        """
        super(Downloader, self).__init__()
        self.start_ = start_
        self.end_ = end_
        self.t_id = t_id
        self.url = url
        self.name = name

    def download(self):
        """
        开始下载
        :return:
        """
        print(f'{self.t_id} 开始下载')
        res = requests.get(self.url, headers={'Range': f'Bytes={self.start_}-{self.end_}'}).content
        with open(self.name, 'r+b') as fp:
            fp.seek(self.start_)
            fp.write(res)
        print(f'{self.t_id} 结束下载')

    def run(self):
        """
        开始运行
        :return:
        """
        self.download()


def cost(func):
    def wrapper(*args, **kwargs):
        print('文件开始开始下载')
        s = time.time()
        execute = func(*args, **kwargs)
        e = time.time()
        print(f'下载结束, 用时: {round(e - s, 2)} s')
        return execute

    return wrapper


@cost
def main(url: str, threads: int = 4):
    """
    处理各种数据
    :param url: 资源地址
    :param threads: 线程数
    :return:
    """
    try:
        res = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('资源连接错误')
        sys.exit(-1)
    if res.status_code == 302:
        url = res.headers['Location']
        print(f'资源已重定向到: {url}')
    file_name = url.split('/')[-1]
    open(file_name, 'w').close()
    file_size = int(res.headers['Content-Length'])
    offset = file_size // threads
    start = 0
    for i in range(threads):
        if i == 0:
            end = offset
        elif i == threads - 1:
            end = file_size
        else:
            end = i * offset
        t = Downloader(start, end, i, url, file_name)
        t.start()
        t.join()
        start = end


if __name__ == '__main__':
    main('https://i0.hdslb.com/bfs/archive/ef0945f7d54a505953272022063a6335a9d3becf.jpg')

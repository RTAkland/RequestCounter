#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/18
# @File Name: packlog.py


import os
import time
import tarfile


def make_targz():
    """
    打包为tar.gz
    压缩文件
    :return:
    """
    output_dir = f'./static/cache/{time.strftime("%Y-%m-%d %H")}.tar.gz'
    tar = tarfile.open(output_dir, 'w:gz')
    for root, dir, files in os.walk('./bin/log'):
        for file in files:
            pathfile = os.path.join(root, file)
            tar.add(pathfile)
    tar.close()


__all__ = ['make_targz']
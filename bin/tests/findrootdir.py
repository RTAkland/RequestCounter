#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/16
# @File Name: findrootdir.py


import os


class Checkout:
    def __init__(self, path: str):
        self.path = path.split('/')[:-1]

    def checkout_path(self, path: str):
        if os.path.exists(f'{path}/utils'):
            return True
        else:
            return False

    def run(self):
        for i in range(len(self.path)):
            current_path = '/'.join('/'.join(self.path).split('/')[:-i])
            if self.checkout_path(current_path):
                return current_path



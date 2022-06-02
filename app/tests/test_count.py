#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/5/1
# @File Name: test_count.py


import requests
import unittest


class TestCount(unittest.TestCase):
    def setUp(self) -> None:
        self.api = 'http://127.0.0.1:5000/'

    def test_index(self):
        res = requests.post(self.api).text
        self.assertIsNotNone(res)

    def test_count(self):
        res = requests.post(self.api + 'count/test-example').text
        self.assertIsNotNone(res)

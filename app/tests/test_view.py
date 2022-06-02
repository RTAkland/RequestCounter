#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/5/2
# @File Name: test_view.py


import random
import requests
import unittest


class TestViews(unittest.TestCase):
    def setUp(self) -> None:
        self.api = 'http://127.0.0.1:5000/'

    @property
    def r_name(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        r_name = [random.choice(letters) for _ in range(10)]
        return r_name

    def test_not_found(self):
        res = requests.get(self.api + 'not_exist_page')
        self.assertEqual(res.status_code, 404)

    def test_server_internal_error(self):
        res = requests.get(self.api + f'count/{self.r_name}', params={'length': 0})
        self.assertEqual(res.status_code, 500)

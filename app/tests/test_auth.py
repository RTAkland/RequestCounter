#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/5/2
# @File Name: test_auth.py


import random
import requests
import unittest


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.api = 'http://127.0.0.1:5000/api/v1/'

    @property
    def r_pwd(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        r_pwd = ''.join(random.choice(letters) for _ in range(16))
        return r_pwd

    def test_api_system_header(self):
        res = requests.post(self.api + 'system', headers={'Authorization': 'bearer unittest'})
        self.assertEqual(res.status_code, 200)

    def test_api_system_query(self):
        res = requests.post(self.api + 'system', params={'key': 'unittest'})
        self.assertEqual(res.status_code, 200)

    def test_api_system_header_failed(self):
        res = requests.post(self.api + 'system', headers={'Authorization': f'bearer {self.r_pwd}'})
        self.assertEqual(res.status_code, 403)

    def test_api_system_query_failed(self):
        res = requests.post(self.api + 'system', params={'key': self.r_pwd})
        self.assertEqual(res.status_code, 403)

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/5/1
# @File Name: test_api.py


import random
import unittest
import requests


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.api = 'http://127.0.0.1:5000/api/v1/'

    def test_query(self):
        res = requests.post(self.api + 'query', params={'name': 'test-example'})
        self.assertEqual(res.status_code, 200)

    def test_query_failed(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r_name = ''.join(random.choice(letters) for _ in range(10))
        res = requests.post(self.api + 'query', params={'name': r_name})
        self.assertEqual(res.status_code, 404)

    def test_overall(self):
        res = requests.post(self.api + 'overall')
        self.assertEqual(res.status_code, 200)

    def test_alltables(self):
        res = requests.post(self.api + 'alltables')
        self.assertEqual(res.status_code, 200)

    def test_test(self):
        res = int(requests.post(self.api + 'test').text)
        self.assertIs(type(res), int)

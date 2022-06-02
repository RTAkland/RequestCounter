#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/5/1
# @File Name: test_resources.py


import requests
import unittest


class TestResources(unittest.TestCase):
    def setUp(self) -> None:
        self.resources_urls = {
            'docs': [
                'https://request-counter-docs.vercel.app/#/',
                'https://markusjoe.github.io/RequestCounter/#/'
            ],
            'database': 'https://filebase.vercel.app/download/data.sqlite',
            'themes':
                {
                    'lewd': 'https://static-file-hosting.vercel.app/static/lewd/0',
                    'gelbooru': 'https://static-file-hosting.vercel.app/static/gelbooru/0',
                    'moebooru': 'https://static-file-hosting.vercel.app/static/moebooru/0',
                    'blacked': 'https://static-file-hosting.vercel.app/static/blacked/0',
                    'lisu': 'https://static-file-hosting.vercel.app/static/lisu/0'
                }
        }

    def test_doc_vercel(self):
        res = requests.post(self.resources_urls['docs'][0]).text
        self.assertIsNotNone(res)

    def test_doc_github(self):
        res = requests.post(self.resources_urls['docs'][1]).text
        self.assertIsNotNone(res)

    def test_database(self):
        res = requests.post(self.resources_urls['database'])
        self.assertEqual(res.status_code, 200)

    def test_themes(self):
        for t in self.resources_urls['themes']:
            res = requests.get(self.resources_urls['themes'][t])
            self.assertEqual(res.status_code, 200)

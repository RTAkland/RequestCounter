#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: Pycharm
# @Create Time: 2022/4/29
# @File Name: update.py


import os
import base64
import logging
import requests
from ..config import VersionConfig
from typing import Dict, List


class SelfUpdateVersion:
    """更新本体 -> 更新单个文件"""

    def __init__(self, logger: logging.Logger):
        self.api = 'https://api.github.com/repos/MarkusJoe/RequestCounter/tags'
        self.headers = {'Authorization': 'token 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'}
        self.resp = requests.get(self.api, headers=self.headers).json()
        self.logger = logger

    def commit_details(self):
        """
        获取提交细节
        :return:
        """
        commit_url = self.resp[0]['commit']['url']
        res = requests.get(commit_url, headers=self.headers).json()
        files = res['files']
        modified = []
        deleted = []

        for f in files:
            file_path = f['filename']
            base64_content = requests.get(f['contents_url'], headers=self.headers).json()['content']  # 直接获取修改文件的base64
            if f['status'] in ['modified', 'added']:
                modified.append({'filename': f'./{file_path}', 'content': base64.b64decode(base64_content)})
            else:
                deleted.append(f'./{file_path}')

        self.apply_change(modified, deleted)

    def apply_change(self, modified: List[Dict], deleted: List):
        """
        应用已经更改的文件
        :param modified:
        :param deleted:
        :return:
        """
        for d in deleted:
            os.remove(d)
            self.logger.info(f'删除了: {d}')

        for m in modified:
            with open(m['filename'], 'wb') as modify:
                modify.write(m['content'])
                self.logger.info(f'修改了: {m["filename"]}')

        with open('./app/config.py', 'wb') as update_config:
            content = requests.get('https://api.github.com/repos/MarkusJoe/RequestCounter/contents/app/config.py',
                                   headers=self.headers).json()['content']
            update_config.write(base64.b64decode(content))

        exit()

    def check(self):
        current = VersionConfig.version[0]
        newest = self.resp[0]['name']
        if current != newest:
            self.logger.warning(f'当前版本已经落后于最新版本. 当前: {current} -> 远程: {newest}')
            self.commit_details()
            return False
        else:
            self.logger.info('当前版本为最新版本')
            return True

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/12
# @File Name: __init__.py


import os
from bin.utils.logger import logger
from bin.utils.settings import Settings

if __name__ != '__main__':
    if Settings().type.lower() == 'mysql' and not os.path.exists('./static/origin.sql'):
        logger.warning('当前使用的数据库为MySQL请前往 https://themedatabase.vercel.app/source/sql 下载sql文件')
        logger.warning('并使用 source 命令来导入MySQL数据库')
        logger.warning('此消息只显示一次, 下次启动不显示')
        open('./static/origin.sql', 'w').close()

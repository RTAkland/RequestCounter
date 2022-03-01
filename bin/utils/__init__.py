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
    if Settings().type == 'MySQL' and not os.path.exists('./bin/db/origin.sql'):
        logger.info('当前使用的数据库为MySQL请前往 https://themedatabase.vercel.app/source/sql 下载sql文件')
        logger.info('并使用 source 命令来导入MySQL数据库')
        logger.info('忽略此消息请在./bin/db内创建一个名为origin.sql的文件')

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/4
# @File Name: __init__.py.py


import os
from bin.utils.logger import logger

if not os.path.exists('./bin/db/count.db'):
    logger.error('未检测到用户计数数据库')
    import sqlite3
    conn = sqlite3.connect('./bin/db/count.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('create table ReqCount (name text primary key, times int)')
    conn.commit()
    cursor.close()
    conn.close()
    logger.info('已在./db 目录下创建了count.db数据库')

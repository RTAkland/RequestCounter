#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/5
# @File Name: init_db.py

import os
import sqlite3
import sys

if __name__ == '__main__':
    while True:
        yes_or_no = input('该操作会将数据库初始化输入y继续:')
        if yes_or_no == 'y':
            try:
                os.remove('../../db/count.db')
            except PermissionError:
                print('有其他程序正在使用此数据库无法删除')
                sys.exit(-1)
            conn = sqlite3.connect('../../db/count.db')
            cursor = conn.cursor()
            cursor.execute('create table ReqCount (name text primary key, times integer )')
            sys.exit(0)
        elif yes_or_no == 'n':
            print('已取消')
            sys.exit(0)
        else:
            print('请输入y继续或n退出')
            continue

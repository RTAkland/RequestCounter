#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/16
# @File Name: connectdb.py


import sqlite3


def exec(cmd):
    try:
        conn = sqlite3.connect('../../db/count.db')
        cursor = conn.cursor()
        cursor.execute(cmd)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    while True:
        cmd = input('>>>')
        print(exec(cmd))


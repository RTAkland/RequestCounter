#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/4
# @File Name: rne.py


def main(a, **kwargs):
    print(a, kwargs)


if __name__ == '__main__':
    main('sd', temp=1, sd=2)
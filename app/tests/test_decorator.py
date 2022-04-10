#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/10
# @File Name: test_decorator.py


def check(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper


@check()
def test(name: str):
    print(name)


test('Markus')
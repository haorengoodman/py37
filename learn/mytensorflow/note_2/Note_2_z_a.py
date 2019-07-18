#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 14:11
# @Author  : journal
# @File    : Note_2_z_a.py
# @Software: PyCharm
import tensorflow as tf


def test_if():
    age = input("请输入你的年龄:\n")
    if age > 18:
        print("已成年!")
    else:
        print("未成年!")


def test_for():
    for i in range(1, 5):
        print("index:"+str(i))


if __name__ == '__main__':
    # test_if()
    test_for()

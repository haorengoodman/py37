# -*- coding:utf-8 -*-
"""
值传递、引用传递

@author:dell
@file: Day06_04.py
@time: 2020/01/08
"""


# 值传递
def xx(a):
    a += 1
    print(a)


# 引用传递
def oo(b):
    b[0] = 100
    print(b[0])


if __name__ == '__main__':
    a = 100
    xx(a)
    print(a)

    b = [10]
    oo(b)
    print(b[0])

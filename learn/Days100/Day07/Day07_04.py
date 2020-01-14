# -*- coding:utf-8 -*-
"""
字符串格式化

@author:dell
@file: Day07_04.py
@time: 2020/01/08
"""


if __name__ == '__main__':
    a, b = 5, 10
    # 方式一
    print("%d * %d = %d" % (a, b, a*b))
    # 方式二
    print('{0} * {1} = {2}'.format(a, b, a * b))
    # 方式三(Python 3.6 以后)
    print(f'{a} * {b} = {a * b}')

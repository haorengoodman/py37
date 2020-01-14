# -*- coding:utf-8 -*-
"""
range 函数
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量

@author:dell
@file: Day04_01.py
@time: 2020/01/07
"""


def my_print(x):
    for i in x:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    a = range(101)
    b = range(10, 101)
    c = range(1, 100, 2)
    my_print(a)
    my_print(b)
    my_print(c)
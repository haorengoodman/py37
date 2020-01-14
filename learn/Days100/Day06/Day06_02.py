# -*- coding:utf-8 -*-
"""
判断素数

@author:dell
@file: Day06_02.py
@time: 2020/01/08
"""


def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


if __name__ == '__main__':
    print(is_prime(1070))

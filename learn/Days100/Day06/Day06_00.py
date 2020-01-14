# -*- coding:utf-8 -*-
"""
求最大公约数和最小公倍数的函数。

@author:dell
@file: Day06_00.py
@time: 2020/01/08
"""


def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if y > x else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


if __name__ == '__main__':
    x = 14
    y = 21
    res = gcd(x, y)
    res1 = lcm(x, y)
    print(res)
    print(res1)

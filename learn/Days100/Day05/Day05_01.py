# -*- coding:utf-8 -*-
"""
正整数的反转
将12345变成54321

@author:dell
@file: Day05_01.py
@time: 2020/01/07
"""

if __name__ == '__main__':
    a = int(input("请输入一个正整数:"))
    n = 0
    result = 0
    while a > 0:
        n += 1
        b = a % 10
        result = result * 10 + b
        a //= 10
    print(result)
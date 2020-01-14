# -*- coding:utf-8 -*-
"""
判断输入的正整数是不是回文素数

@author:dell
@file: Day06_03.py
@time: 2020/01/08
"""
from com.Days100.Day06.Day06_02 import is_prime
from com.Days100.Day06.Day06_01 import is_palindrome


def my_func(num):
    return is_prime(num) and is_palindrome(num)


if __name__ == '__main__':
    print(my_func(101))
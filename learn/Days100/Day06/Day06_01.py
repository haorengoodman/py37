# -*- coding:utf-8 -*-
"""
判断是否为回文数(反转后与原数字相同)

@author:dell
@file: Day06_01.py
@time: 2020/01/08
"""


def reverse_num(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10
    return result


def is_palindrome(num):
    return reverse_num(num) == num


if __name__ == '__main__':
    r = is_palindrome(10)
    print(r)

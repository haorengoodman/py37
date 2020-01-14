# -*- coding:utf-8 -*-
"""
构造程序逻辑
寻找水仙花数。
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：1^3 + 5^3+ 3^3=153。

@author:dell
@file: Day05_00.py
@time: 2020/01/07
"""

if __name__ == '__main__':
    for i in range(100, 1000):
        low = i % 10
        mid = int(i / 10) % 10
        high = i // 100  # int(i / 100)
        temp = low ** 3 + mid ** 3 + high ** 3
        if i == temp:
            print(i, high, mid, low)

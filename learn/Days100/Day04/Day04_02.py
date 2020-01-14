# -*- coding:utf-8 -*-
"""
用for循环实现1~100之间的偶数求和

@author:dell
@file: Day04_02.py
@time: 2020/01/07
"""

if __name__ == '__main__':
    a = range(2, 101, 2)
    sum = 0
    for i in a:
        sum += i
    print(sum)
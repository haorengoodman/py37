# -*- coding:utf-8 -*-
"""
字符串切片
[index] ： 获取指定位置的字符
[beginIndex:endIndex] : 前闭后开的区间
[beginIndex:endIndex:step] :开始索引位置:结束索引位置:步长

@author:dell
@file: Day07_02.py
@time: 2020/01/08
"""


if __name__ == '__main__':
    s = "0123456789"
    print(s[3])
    print(s[2:5])
    print(s[2:])
    print(s[2::2])
    print(s[::2])
    print(s[::-1])
    print(s[-3:-1])
    print(s[-1:-3:-1])

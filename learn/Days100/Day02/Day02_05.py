# -*- coding:utf-8 -*-
"""
练习3：输入年份判断是不是闰年。

@author:dell
@file: Day02_05.py
@time: 2020/01/07
"""

if __name__ == '__main__':
    year = int(input('请输入年份: '))
    # 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
    is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    print(is_leap)

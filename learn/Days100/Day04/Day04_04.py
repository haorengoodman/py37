# -*- coding:utf-8 -*-
"""
输出乘法口诀表(九九表)

@author:dell
@file: Day04_04.py
@time: 2020/01/07
"""

if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i+1):
            print("%d*%d=%d" % (j, i, i * j), end='\t')
        print()

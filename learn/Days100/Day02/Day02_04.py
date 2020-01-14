# -*- coding:utf-8 -*-
"""
练习2：输入圆的半径计算计算周长和面积。
perimeter = 2 * pi * r
area = pi * r * r

@author:dell
@file: Day02_04.py
@time: 2020/01/07
"""
import math

if __name__ == '__main__':
    radius = float(input('请输入圆的半径: '))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print("半径 r = %.1f 的周长为: %.1f" % (radius, perimeter))
    print("半径 r = %.1f 的面积为: %.1f" % (radius, area))
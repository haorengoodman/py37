# -*- coding:utf-8 -*-
"""
练习1：华氏温度转换为摄氏温度
华氏温度到摄氏温度的转换公式为：C=(F - 32) div 1.8

@author:dell
@file: Day02_03.py
@time: 2020/01/07
"""
if __name__ == '__main__':
    a = float(input("请输入华氏温度: "))
    b = (a - 32) / 1.8
    print("华氏温度：%.1f = 摄氏温度：%.1f" % (a, b))




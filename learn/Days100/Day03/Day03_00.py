# -*- coding:utf-8 -*-
"""
分支结构
练习1：英制单位英寸与公制单位厘米互换。

@author:dell
@file: Day03_00.py
@time: 2020/01/07
"""
if __name__ == '__main__':
    value = float(input("请输入长度："))
    unit = str(input("请输入单位："))
    if unit == "in" or unit == "英寸":
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效的单位')
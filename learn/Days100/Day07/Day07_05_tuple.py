# -*- coding:utf-8 -*-
"""
python 数据结构 ： tuple
1. 元组中的元素是无法修改的
2. 元组在创建时间和占用的空间上面都优于列表

@author:dell
@file: Day07_05_tuple.py
@time: 2020/01/08
"""

if __name__ == '__main__':
    t = ("jack", "马", 54)
    print(t)
    print(type(t))
    print(t[2])
    for i in t:
        print("遍历方法:"+str(i))
    t = ("jack", "成", 64)  # 变量t重新引用了新的元组原来的元组将被垃圾回收
    print(t)
    person = list(t)  # 将元组转换成列表
    print(person)
    print(type(person))

    # list -> tuple
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(type(fruits_tuple))

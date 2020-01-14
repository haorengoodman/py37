# -*- coding:utf-8 -*-
"""
python 数据结构 ： set

@author:dell
@file: Day07_05_set.py
@time: 2020/01/08
"""

if __name__ == '__main__':
    # 创建集合的字面量语法
    set1 = {1, 2, 3}
    # 创建集合的构造器语法(面向对象部分会进行详细讲解)
    set2 = set(range(10))
    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set3 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}

    # 向集合添加元素和从集合删除元素。
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    set2.discard(5)  # 元素存在，则删除，不存在，则不作任何操作
    if 4 in set2:
        set2.remove(4)  # 元素存在，则删除，元素不存在，则抛出异常
    print(set1, set2)
    print(set3.pop())
    print(set3)

    # 集合的成员、交集、并集、差集等运算。
    print("交叉并补")
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)  # 补集
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


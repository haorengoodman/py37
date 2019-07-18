#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 11:07
# @Author  : journal
# @File    : Note_2_0_list.py
# @Software: PyCharm


# 列表  使用[]初始化
def test_list():
    list_1 = [1, 2, 3, 4, 5, 6, 7]
    # 1.切片
    # 切片[beginIndex:endIndex) 前闭后开
    # 切片[beginIndex:endIndex:step]
    print(list_1)          # [1, 2, 3, 4, 5, 6, 7]
    print(list_1[1:3])     # [2, 3]
    print(list_1[0:3])     # [1, 2, 3]
    print(list_1[0:3:2])   # [1, 3]
    print(list_1[1:6:2])   # [2, 4, 6]
    print(list_1[1:6:3])   # [2, 5]
    # -1 表示列表中的最后一个元素,倒数第二个元素为-2 ，依此类推
    print(list_1[-1:0:-3])   # [7, 4]
    print(list_1[-1::-3])    # [7, 4, 1]
    print(list_1[-2::-3])    # [6, 3]
    # 2.索引
    print(list_1[0])
    # 3.插入(在index=7 的位置插入value=8)
    list_1.insert(7, 8)
    print(list_1)
    # 4.删除(index=8位置的数据)
    del list_1[7]
    print(list_1)


if __name__ == '__main__':
    test_list()

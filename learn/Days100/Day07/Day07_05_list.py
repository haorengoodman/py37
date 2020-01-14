# -*- coding:utf-8 -*-
"""
python 数据结构 ： list


@author:dell
@file: Day07_05_list.py
@time: 2020/01/08
"""

if __name__ == '__main__':
    # 创建方式一
    list1 = list("abcde")
    # 创建方式二
    list2 = [1, 2, 3]

    # 遍历
    for ele in list1:
        print(ele)
    for i in range(len(list2)):
        print(list2[i])
    for i, ele in enumerate(list2):
        print(i, ele)

    # 切片操作
    print("切片操作")
    print(list1[1:2])
    print(list1[1:4])
    print(list1[1:])
    print(list1[:4])
    print(list1[-3])
    print(list1[::-1])  # 翻转
    print(list1[:])  # 实现拷贝

    # list 增
    list3 = [1, 5, 3, 90, 100, 30]
    list3.append(30)  # 末尾添加元素
    list3.insert(1, 400)  # 在指定位置添加元素
    list4 = [55, 66]
    list3 += list4  # list 合并

    # list 删除指定元素(如果该元素是重复元素， 只删除第一个)
    if 30 in list3:
        list3.remove(30)
    print(list3)
    # list 删除指定索引的元素
    list3.pop(0)
    print(list3)
    # 清空list
    list3.clear()
    print(list3)

    # list排序
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)

    # 生成式
    import sys
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)

    # 生成器(注意：list1 的类型为：generator)
    def my_list():
        for i in range(100):
            yield i*2
    list1 = my_list()
    print(type(list1))
    for x in list1:
        print(x, end=" ")




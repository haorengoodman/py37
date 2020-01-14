# -*- coding:utf-8 -*-
"""
字符串常用方法总结

@author:dell
@file: Day07_03.py
@time: 2020/01/08
"""


if __name__ == '__main__':
    s = "hello world!"
    print(len(s))  # 计算字符串长度
    print(s.capitalize())  # 获得首字母大写副本
    print(s.title())   # 获得字符串中每个单词首字母大写副本
    print(s.upper())  # 获得字符串大写副本
    print(s.find("ll"))  # 获得子串索引位置 (-1 表示未找到)
    print(s.startswith("he"))  # 判断是否以指定子串开头
    print(s.endswith("he"))  # 判断是否以指定子串结尾
    print(s.center(50, "*"))   # 字符串居中，两侧填充指定字符(总长度为50)
    print(s.rjust(50, "-"))
    print(s.ljust(50, "^"))
    print(s.isdigit())  # 判断字符串是否为纯数字
    print("123".isdigit())
    print(s.isalpha())  # 判断字符串是否纯字母
    print("aaa".isalpha())
    print(s.isalnum())  # 判断是否为数字和字母的组合
    print("12a".isalnum())
    print(" xx ".strip())  # 去除两端空格



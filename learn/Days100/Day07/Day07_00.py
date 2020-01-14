# -*- coding:utf-8 -*-
"""
字符串转义

@author:dell
@file: Day07_00.py
@time: 2020/01/08
"""

s = """a = 100
b = 200
"""
if __name__ == '__main__':
    # 使用\（反斜杠）来表示转义
    print(s)
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u9a86\u660a'
    print(s1, s2)

    # 不希望字符串中的\表示转义   在字符串的最前面加上字母r
    s1 = r'\141\142\143\x61\x62\x63'
    s2 = r'\u9a86\u660a'
    print(s1, s2, end='\t')


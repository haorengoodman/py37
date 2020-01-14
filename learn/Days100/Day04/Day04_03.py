# -*- coding:utf-8 -*-
"""
while  循环
猜数字游戏
break 终止循环
continue 终止本次循环，继续执行下一次循环

@author:dell
@file: Day04_03.py
@time: 2020/01/07
"""
import random

if __name__ == '__main__':
    a = random.randint(0, 100)
    count = 0
    while True:
        b = int(input("请输入一个整数(0-100):"))
        count += 1
        if b > a:
            print("大了")
        elif b < a:
            print("小了")
        else:
            print("对了")
            print("您一共猜了%d次" % count)
            break
    if count > 7:
        print('你的智商余额明显不足')


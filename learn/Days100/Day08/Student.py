# -*- coding:utf-8 -*-
"""
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头。
建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的.不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作

@author:dell
@file: Student.py
@time: 2020/01/13
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


if __name__ == '__main__':
    s1 = Student("jack", 50)
    s1.study("哲学")
    s1.watch_movie()

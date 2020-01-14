# -*- coding:utf-8 -*-
"""
Python 从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）

@author:dell
@file: Person.py
@time: 2020/01/13
"""
from abc import ABCMeta, abstractmethod


class Person(object, metaclass=ABCMeta):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @abstractmethod
    def xx(self):
        pass


if __name__ == '__main__':
    p = Person("jack", 30)

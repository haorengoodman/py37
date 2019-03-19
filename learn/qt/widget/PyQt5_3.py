#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:47
# @Author  : journal
# @File    : PyQt5_3.py
# @Software: PyCharm

__author__ = 'journal'


import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv) # 必须创建一个应用程序对象
    # print(sys.argv) # 第一个参数为运行程序的全路径
    # print(len(sys.argv)) # 查看系统参数长度

    # 没有父类口小部件称为窗口。
    w = QWidget() # 窗口组件
    w.resize(450, 300) # 宽、高
    w.move(600, 300) # 宽、高(距左上角)
    w.setWindowTitle('PyQt5') # 设置title
    w.show() # 在屏幕上显示窗口小部件

    sys.exit(app.exec_())

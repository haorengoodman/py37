#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_5.py
# @Date    : 2019-02-15
# @Author  : gaotao
import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMessageBox, QLCDNumber, QDial, QSlider


# 信号、槽
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 创建 QLCDNumber、QDial、slider
        self.lcd = QLCDNumber(self)
        self.dial = QDial(self)
        self.slider = QSlider(self)
        # 设定各个部件属性
        self.initUI()

    def initUI(self):
        # 设置窗口
        self.setWindowTitle("信号、槽")
        self.setGeometry(300,300,300,200)
        # 设置 QLCDNumber、QDial
        self.lcd.setGeometry(115,50,70,40)
        self.dial.setGeometry(80,120,70,70)
        self.slider.setGeometry(190,120,20,70)
        # 事件绑定
        self.dial.valueChanged.connect(self.lcd.display)
        self.slider.valueChanged.connect(self.lcd.display)
        # 窗口显示
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())


#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_6_1.py
# @Date    : 2019-02-16
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout


# 自定义布局  拉伸因子 stretch，通过拉伸因子来控制 指定空白 被切分为多少等分
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.bt1 = QPushButton("剪刀", self)
        self.bt2 = QPushButton("石头", self)
        self.bt3 = QPushButton("布", self)
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setGeometry(200, 200, 500, 350)
        self.setWindowTitle('自定义布局')
        # 设置窗口布局
        # 水平方向的空白被分成了6等份儿
        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)
        hbox.addWidget(self.bt3)
        hbox.addStretch(2)
        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # 将布局添加到窗口
        self.setLayout(vbox)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

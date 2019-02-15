#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_6_0.py
# @Date    : 2019-02-15
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout


# 自定义布局
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.bt1 = QPushButton("剪刀", self)
        self.bt2 = QPushButton("石头", self)
        self.bt3 = QPushButton("布", self)
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('自定义布局')
        # 设置窗口布局
        hbox = QHBoxLayout()  # 水平布局
        hbox.addStretch(1)  # 添加拉伸因子
        hbox.addWidget(self.bt1)
        hbox.addWidget(self.bt2)
        hbox.addWidget(self.bt3)
        vbox = QVBoxLayout()  # 垂直布局
        vbox.addStretch(1)  # 添加拉伸因子
        vbox.addLayout(hbox)
        self.setLayout(vbox)  # 使用布局
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

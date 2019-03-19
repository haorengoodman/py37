#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_5_1.py
# @Date    : 2019-02-15
# @Author  : gaotao
import sys
from random import randint
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMessageBox, QLCDNumber, QDial, QSlider, \
    QLabel


# 方向展示
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 创建 QLabel
        self.lab = QLabel('方向', self)
        # 设定各个部件属性
        self.initUI()

    def initUI(self):
        # 设置窗口
        self.setWindowTitle("信号、槽")
        self.setGeometry(300,300,300,200)
        # QLabel属性设置
        self.lab.setGeometry(115, 70, 70, 40)
        # 窗口显示
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText("↑")
        elif e.key() == Qt.Key_Left:
            self.lab.setText("←")
        elif e.key() == Qt.Key_Down:
            self.lab.setText("↓")
        elif e.key() == Qt.Key_Right:
            self.lab.setText("→")
        else:
            self.lab.setText("o(╥﹏╥)o")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())


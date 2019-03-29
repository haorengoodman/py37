#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 10:50
# @Author  : journal
# @File    : QtPushButton_2.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout


# PyQt5按钮系列 - 普通按钮(QPushButton)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(1400, 200, 300, 300)
        self.setWindowTitle("普通按钮 - QPushButton")
        #


    def my_click(self):
        QMessageBox.information(self, "title", "btnzz")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

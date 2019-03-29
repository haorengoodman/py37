#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 10:50
# @Author  : journal
# @File    : QtPushButton.py
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

        # 创建 button,并制定快捷键 (alt + D)
        self.btn = QPushButton("Down(&D)", self)

        # 设置样式
        vbox = QVBoxLayout()  # 垂直布局
        vbox.addStretch(1)
        vbox.addWidget(self.btn)

        hbox = QHBoxLayout()  # 水平布局
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.setLayout(hbox)
        # btn 绑定事件
        self.btn.clicked.connect(self.my_click)
        self.show()

    def my_click(self):
        QMessageBox.information(self, "title", "btnzz")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

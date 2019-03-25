#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 15:18
# @Author  : journal
# @File    : QtQRadioButton.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QButtonGroup, QHBoxLayout, QVBoxLayout


# PyQt5按钮系列 - 单选按钮(QRadioButton)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(1400, 200, 300, 300)
        self.setWindowTitle('单选按钮 - RadioButton')

        # 创建 单选按钮
        self.rb_1 = QRadioButton("男", self)
        self.rb_2 = QRadioButton("女", self)
        self.rb_3 = QRadioButton("妖", self)

        # 创建 ButtonGroup，并将单选按钮加入到该组（组内互斥）
        self.bg_1 = QButtonGroup(self)
        self.bg_1.addButton(self.rb_1, 11)
        self.bg_1.addButton(self.rb_2, 22)
        self.bg_1.addButton(self.rb_3, 33)

        # 创建布局
        hbox = QHBoxLayout()  # 水平布局
        hbox.addStretch(1)
        hbox.addWidget(self.rb_1)
        hbox.addStretch(1)
        hbox.addWidget(self.rb_2)
        hbox.addStretch(1)
        hbox.addWidget(self.rb_3)
        hbox.addStretch(1)
        vbox = QVBoxLayout()  # 垂直布局
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


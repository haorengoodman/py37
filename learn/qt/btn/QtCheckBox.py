#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 15:03
# @Author  : journal
# @File    : QtCheckBox.py
# @Software: PyCharm

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


# PyQt5按钮系列 - 复选框(QCheckBox)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 创建复选框
        self.cb1 = QCheckBox("全选", self)
        self.cb2 = QCheckBox("a", self)
        self.cb3 = QCheckBox("b", self)
        self.cb4 = QCheckBox("c", self)
        self.bt = QPushButton("提交", self)

        # 设置布局
        vbox = QVBoxLayout()  # 垂直布局
        vbox.addWidget(self.cb1)
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.cb3)
        vbox.addWidget(self.cb4)
        vbox.addWidget(self.bt)
        hbox = QHBoxLayout()  # 水平布局
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.setLayout(hbox)
        self.show()

        # CheckBox 增加事件绑定
        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        # btn 增加时间绑定
        self.bt.clicked.connect(self.btn_click)

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)

    def changecb2(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            self.cb1.setTristate(True)  # 设置状态(半选中)生效,注:正常状态下，只有选中、非选中这两种状态，通过 setTristate 实现 增加第三种状态 半选中
            self.cb1.setCheckState(Qt.PartiallyChecked)  # 设置半选状态
        else:
            self.cb1.setTristate(False)
            self.cb1.setCheckState(Qt.Unchecked)

    def btn_click(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'title', 'content-全选')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self, 'title', 'content-a,b')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'title', 'content-a,c')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'title', 'content-b,c')
        elif self.cb2.isChecked():
            QMessageBox.information(self, 'title', 'content-a')
        elif self.cb3.isChecked():
            QMessageBox.information(self, 'title', 'content-b')
        elif self.cb4.isChecked():
            QMessageBox.information(self, 'title', 'content-c')
        else:
            QMessageBox.information(self, 'title', 'content-没有任何选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

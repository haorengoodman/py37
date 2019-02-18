#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_6_3.py
# @Date    : 2019-02-18
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit


# 表单布局
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口属性
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('表单布局')
        # 创建并设置表单布局
        formLayout = QFormLayout()
        nameLabel = QLabel("姓名:")
        nameLineEdit = QLineEdit("")
        formLayout.addRow(nameLabel, nameLineEdit)
        descLabel = QLabel("简介:")
        descTextEdit = QTextEdit("")
        formLayout.addRow(descLabel, descTextEdit)
        # 使用布局
        self.setLayout(formLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

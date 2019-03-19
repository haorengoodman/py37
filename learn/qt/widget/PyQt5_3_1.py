#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_3_1.py
# @Date    : 2019-02-14
# @Author  : gaotao
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QT Learning")
        self.setGeometry(300, 200, 300, 300)
        self.setWindowIcon(QIcon("D:/aaaa/image/111057717_title0h.jpg"))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ico = Ico()
    sys.exit(app.exec_())


#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_3_1.py
# @Date    : 2019-02-14
# @Author  : gaotao
import sys
from random import randint

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMessageBox


# 猜数字游戏
class Ico(QWidget):
    text: QLineEdit
    btn: QPushButton

    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        self.setWindowTitle("猜数字")
        self.setGeometry(300, 300, 300, 220)

        self.btn = QPushButton("我猜", self)
        self.btn.setGeometry(115, 150, 70, 30)
        self.btn.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(75, 50, 150, 30)

        self.show()

    def showMessage(self):
        guessNum = int(self.text.text())
        print("输入数字为：{0}".format(guessNum))
        if guessNum > self.num:
            QMessageBox.about(self, "结果", "猜大了！")
            self.text.setFocus()
        elif guessNum < self.num:
            QMessageBox.about(self, "结果", "猜小了！")
            self.text.setFocus()
        else:
            QMessageBox.about(self, "结果", "猜对了！")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ico = Ico()
    sys.exit(app.exec_())


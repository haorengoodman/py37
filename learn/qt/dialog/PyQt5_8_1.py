#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_8_1.py
# @Date    : 2019-02-19
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QIcon

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit, QMainWindow, QAction, QMenu, QInputDialog, QTextBrowser, \
    QFileDialog, QFontDialog, QColorDialog


# 软件界面DIY - 颜色(QColorDialog)、字体(QFontDialog)、打开文件(QFileDialog) 对话框
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200,500, 300)
        self.setWindowTitle('软件界面 DIY')

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(10,10,350,280)

        self.btn1 = QPushButton("选择文件",self)
        self.btn1.setGeometry(400,20,70,30)

        self.btn2 = QPushButton("选择字体",self)
        self.btn2.setGeometry(400,90,70,30)

        self.btn3 = QPushButton("选择颜色",self)
        self.btn3.setGeometry(400,160,70,30)

        self.btn1.clicked.connect(self.clkAct)
        self.btn2.clicked.connect(self.clkAct)
        self.btn3.clicked.connect(self.clkAct)

        self.show()

    def clkAct(self,event):
        sender = self.sender()
        if self.btn1 == sender:
            # fname = QFileDialog.getOpenFileName(self,"title","./")
            # 打开指定后缀的文件
            fname = QFileDialog.getOpenFileName(self,"title","./", ("python (*.pyx)"))
            if fname[0]:
                with open(fname[0],mode='r',encoding='utf-8',errors='ignore') as f:
                    self.textedit.setText(f.read())
        if self.btn2 == sender:
            font, ok = QFontDialog.getFont()
            if ok:
                self.textedit.setFont(font)
        if self.btn3 == sender:
            color = QColorDialog.getColor()
            if color.isValid():
                self.textedit.setTextColor(color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

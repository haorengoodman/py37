#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_8_0.py
# @Date    : 2019-02-19
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QIcon

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit, QMainWindow, QAction, QMenu, QInputDialog, QTextBrowser


# 软件界面DIY - 标准输入对话框(QInputDialog)
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200,400, 300)
        self.setWindowTitle('软件界面 DIY')

        self.label_1 = QLabel("姓名",self)
        self.btn_1 = QPushButton("修改姓名",self)
        self.label_1.setGeometry(100,10,50,30)
        self.btn_1.setGeometry(200,10,70,30)
        self.btn_1.clicked.connect(self.clickAct)

        self.label_2 = QLabel("年龄",self)
        self.btn_2 = QPushButton("修改年龄",self)
        self.label_2.setGeometry(100,50,50,30)
        self.btn_2.setGeometry(200,50,70,30)
        self.btn_2.clicked.connect(self.clickAct)

        self.label_3 = QLabel("性别",self)
        self.btn_3 = QPushButton("修改性别",self)
        self.label_3.setGeometry(100,90,50,30)
        self.btn_3.setGeometry(200,90,70,30)
        self.btn_3.clicked.connect(self.clickAct)

        self.label_4 = QLabel("身高",self)
        self.btn_4 = QPushButton("修改身高",self)
        self.label_4.setGeometry(100,130,50,30)
        self.btn_4.setGeometry(200,130,70,30)
        self.btn_4.clicked.connect(self.clickAct)

        self.label_5 = QLabel("简介",self)
        self.btn_5 = QPushButton("修改简介",self)
        self.textBrowser = QTextBrowser(self)
        self.label_5.setGeometry(100,170,50,30)
        self.btn_5.setGeometry(200,170,70,30)
        self.textBrowser.setGeometry(100,210,170,70)
        self.btn_5.clicked.connect(self.clickAct)

        self.show()

    #注 QInputDialog.getOoxx(QWidget,title,提示词,.....)
    def clickAct(self,event):
        sender = self.sender()
        if sender == self.btn_1:
            text, ok = QInputDialog.getText(self,"修改姓名","请输入姓名:")
            if ok:
                self.label_1.setText(text)
        if sender == self.btn_2:
            text, ok = QInputDialog.getInt(self,'修改年龄', '请输入年龄：', min = 1)
            if ok:
                self.label_2.setText(str(text))
        if sender == self.btn_3:
            text, ok = QInputDialog.getItem(self,"修改性别","请选择性别",['男','女'])
            if ok:
                self.label_3.setText(text)
        if sender == self.btn_4:
            text, ok = QInputDialog.getDouble(self,"修改身高","修改身高",min=1.0)
            if ok:
                self.label_4.setText(str(text))
        if sender == self.btn_5:
            text, ok = QInputDialog.getMultiLineText(self,"修改简介","修改简介")
            if ok:
                self.textBrowser.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

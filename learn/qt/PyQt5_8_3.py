#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_8_3.py
# @Date    : 2019-02-20
# @Author  : gaotao
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys


# 软件界面DIY - 消息对话框(QMessageDialog)
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200,500, 400)
        self.setWindowTitle('软件界面 DIY')

        self.lab = QLabel("显示按钮类型信息",self)
        self.lab.move(20,20)

        self.bt1 = QPushButton("提示",self)
        self.bt1.move(20,70)
        self.bt2 = QPushButton("询问",self)
        self.bt2.move(20,120)
        self.bt3 = QPushButton("警告",self)
        self.bt3.move(20,170)
        self.bt4 = QPushButton("错误",self)
        self.bt4.move(20,220)
        self.bt5 = QPushButton("关于",self)
        self.bt5.move(20,270)
        self.bt6 = QPushButton("关于QT",self)
        self.bt6.move(20,320)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning2)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()

    def info(self):
        reply = QMessageBox.information(self,"提示","这是一个消息提示对话框!",QMessageBox.Ok|QMessageBox.Close,QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.lab.setText("你选择的是OK")
        else:
            self.lab.setText('你选择了Close！')

    def question(self):
        reply = QMessageBox.question(self,"询问","这是一个消息询问对话框!",QMessageBox.Ok|QMessageBox.Close,QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.lab.setText("你选择的是OK")
        else:
            self.lab.setText('你选择了Close！')

    # 消息对话框实现方式:基于静态函数的调用
    def warning(self):
        reply = QMessageBox.warning(self,"警告","这是一个警告对话框!", QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        if reply == QMessageBox.Save:
            self.lab.setText('你选择了保存！')
        elif reply == QMessageBox.Discard:
            self.lab.setText('你选择了不保存！')
        else:
            self.lab.setText('你选择了取消！')
    # 消息对话框实现方式:基于属性的调用
    def warning2(self):
        # 定制消息对话框
        msgBox = QMessageBox()
        msgBox.setWindowTitle("警告")
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("这是一个警告对话框")
        # 使用Infromative文本来扩展text()以向用户提供更多信息
        msgBox.setInformativeText("setInformativeText方法; informative:详实的")
        # 此处使用的是自定义按钮
        saveBtn = msgBox.addButton("保存",QMessageBox.AcceptRole)
        msgBox.addButton("取消",QMessageBox.RejectRole)
        msgBox.addButton("不保存",QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(saveBtn)

        # 复选框设置
        cb = QCheckBox('所有文档都按此操作')
        msgBox.setCheckBox(cb)
        cb.stateChanged.connect(self.check)

        # 让消息对话框能够显示出来
        reply = msgBox.exec()
        if reply == QMessageBox.AcceptRole:
            self.lab.setText('你选择了保存！')
        elif reply == QMessageBox.RejectRole:
            self.lab.setText('你选择了取消！')
        else:
            self.lab.setText('你选择了不保存！')

    def check(self):
        if self.sender().isChecked():
            self.lab.setText('你打勾了哦')
        else:
            self.lab.setText('怎么又不打了啊')

    def critical(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("错误对话框")
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setIcon(QMessageBox.Critical)
        # 此处使用的是标准按钮
        msgBox.setStandardButtons(QMessageBox.Retry|QMessageBox.Abort|QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        # 该属性保存要在详细信息区域中显示的文本。文本将被解释为纯文本。
        msgBox.setDetailedText("在这里增加详细信息") # 增加 ShowDetails 按钮
        reply = msgBox.exec()
        if reply == QMessageBox.Retry:
            self.lab.setText('你选择了Retry！')
        elif reply == QMessageBox.Abort:
            self.lab.setText('你选择了Abort！')
        else:
            self.lab.setText('你选择了Ignore！')

    def about(self):
        #QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于','卧槽，飞机!')
        msgBox.setIconPixmap(QPixmap("D:/aaaa/image/111057717_title0h.jpg"))
        msgBox.exec()

    def aboutqt(self):
        QMessageBox.aboutQt(self,'关于Qt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

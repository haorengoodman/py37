#!/usr/bin/python

# -*- coding: utf-8 -*-

# @File    : PyQt5_8_2.py
# @Date    : 2019-02-20
# @Author  : gaotao
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrinter, QPrintDialog

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QFormLayout, QLineEdit, QTextEdit, QMainWindow, QAction, QMenu, QInputDialog, QTextBrowser, \
    QFileDialog, QFontDialog, QColorDialog, QDialog


# 软件界面DIY - 打印设置(QPageSetupDialog)、打印(QPrintDialog)打开多个文件对话框
#            - 增强：打开多个文件(QFileDialog)
#            - 保存文件 (QFileDialog)
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200,500, 300)
        self.setWindowTitle('软件界面 DIY')

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(10,10,350,280)

        self.btn1 = QPushButton("打开文件",self)
        self.btn1.setGeometry(400,20,90,30)

        self.btn2 = QPushButton("打开多个文件",self)
        self.btn2.setGeometry(400,70,90,30)

        self.btn3 = QPushButton("保存文件",self)
        self.btn3.setGeometry(400,120,90,30)

        self.btn4 = QPushButton("页面设置",self)
        self.btn4.setGeometry(400,170,90,30)

        self.btn5 = QPushButton("打印文档",self)
        self.btn5.setGeometry(400,220,90,30)

        self.btn1.clicked.connect(self.open_file)
        self.btn2.clicked.connect(self.open_files)
        self.btn3.clicked.connect(self.save_file)
        self.btn4.clicked.connect(self.page_setup)
        self.btn5.clicked.connect(self.print_dialog)

        self.show()

    # getOpenFileName 参数1:父部件;   参数2:说明文字、标题;   参数3:打开目录;   参数4:过滤器，打开指定格式的文件;
    def open_file(self):
        fname = QFileDialog.getOpenFileName(self,caption="打开文件",directory="./",filter='(python (*.py))')
        if fname[0]:
            with open(fname[0],"r",encoding="utf-8",errors="ignore") as f:
                self.textedit.setText(f.read())

    def open_files(self):
        # getOpenFileNames 方法返回值类型 Tuple[List[str], str]
        # 例如: (['C:/10/美文.txt', 'C:/10/十九大(new).txt', 'C:/10/十九大.txt'], '')
        fnames = QFileDialog.getOpenFileNames(self,caption="打开多个文件",directory="./")
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname,"r",encoding="utf-8",errors="ignore") as f:
                    self.textedit.setText(f.read())

    def save_file(self):
        fileName = QFileDialog.getSaveFileName(self,caption="保存文件",directory="./",filter="(python (*.py))")
        if fileName[0]:
            with open(fileName[0],"w",encoding="utf-8",errors="ignore") as f:
                f.write(self.textedit.toPlainText())

    def page_setup(self):
        printsetdialog = QPageSetupDialog(self.printer,self)
        printsetdialog.exec_()

    def print_dialog(self):
        printDialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printDialog.exec_():
            self.textedit.print(self.printer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

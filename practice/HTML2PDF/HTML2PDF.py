# -*- coding:utf-8 -*-
"""
小工具： 将html页面转换为PDF

@author:dell
@file: HTML2PDF.py
@time: 2020/01/16
"""
import os
import sys

import pdfkit
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QFormLayout, QApplication, QLineEdit, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QMessageBox

from practice.HTML2PDF.RoundProgressBar import CircleProgressBar


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.util = MyUtil()
        self.util.my_signal.connect(self.stop_process_bar)
        self.lable_0 = QLabel("url:")
        self.line_text_0 = QLineEdit("https://zhuanlan.zhihu.com/p/94608155")
        self.lable_1 = QLabel("targetPath:")
        self.line_text_1 = QLineEdit(self.get_desk_p())
        self.btn_0 = QPushButton("submit")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("HTML2PDF")
        self.setGeometry(70, 120, 500, 350)
        formLayout = QFormLayout()
        formLayout.addRow(self.lable_0, self.line_text_0)
        formLayout.addRow(self.lable_1, self.line_text_1)

        hbox_0 = QHBoxLayout()
        self.process_bar = CircleProgressBar(self)
        # self.process_bar = CircleProgressBar(self, color=QColor(255, 0, 0), clockwise=False)
        # self.process_bar = CircleProgressBar(self, styleSheet="""qproperty-color: rgb(0, 255, 0);""")
        self.process_bar.hide()
        hbox_0.addWidget(self.process_bar)

        hbox_1 = QHBoxLayout()
        hbox_1.addStretch(3)
        hbox_1.addWidget(self.btn_0)
        hbox_1.addStretch(7)
        self.btn_0.clicked.connect(self.submit_click)  # 绑定事件

        vbox = QVBoxLayout()
        vbox.addLayout(formLayout)
        vbox.addStretch(1)
        vbox.addLayout(hbox_0)
        vbox.addStretch(3)
        vbox.addLayout(hbox_1)

        self.setLayout(vbox)
        self.show()

    # 获取桌面地址
    def get_desk_p(self):
        return os.path.join(os.path.expanduser('~'), "Desktop")

    def submit_click(self):
        self.process_bar.show()
        url = self.line_text_0.text()
        to_file = self.line_text_1.text()
        print(f'url={url} \ntargetPath={to_file}')
        self.util.flag = True
        self.util.url = url
        self.util.to_file = to_file+"\\HTML2PDF.pdf"
        self.util.start()

    def stop_process_bar(self, signal_value):
        if signal_value:
            self.process_bar.hide()
            QMessageBox.information(self, "提示", "保存成功")


class MyUtil(QThread):
    my_signal = pyqtSignal(bool)  # 1
    flag = False
    def url_2_pdf(self):
        # 将 wkhtmltopdf.exe 程序绝对路径传入config对象
        path_wkthmltopdf = 'D:\\myPrograms\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        # 生成 pdf 文件，to_file为文件路径
        pdfkit.from_url(self.url, self.to_file, configuration=config)
        print('完成')
        self.flag = False

    def __init__(self, url=None, to_file=None):
        super().__init__()
        self.url = url
        self.to_file = to_file

    def run(self):
        while self.flag:
            self.url_2_pdf()
            self.my_signal.emit(True)  # 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    sys.exit(app.exec_())


# -*- coding:utf-8 -*-
"""
@author:dell
@file: my_ui.py
@time: 2020/01/14
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QTextBrowser
from pip._vendor import requests


class my_ui(QWidget):
    def __init__(self, name_id_dict):
        super().__init__()
        # name id 映射关系
        self.name_id_dict = name_id_dict
        # 添加组件
        self.label_1 = QLabel("城市:", self)
        self.lineEdit = QLineEdit('北京', self)
        self.textBrowser = QTextBrowser(self)
        self.btn = QPushButton("查询", self)
        self.btn_1 = QPushButton("退出", self)
        # init_ui
        self.init_ui()

    def init_ui(self):
        # 设置样式
        self.setWindowTitle("中国城市天气")
        self.setGeometry(10, 100, 500, 380)  # 前两个表示左上角的位置(宽、高)，后面两个分别表示 宽、高
        self.label_1.setGeometry(140, 20, 70, 30)
        self.lineEdit.setGeometry(180, 20, 140, 30)
        self.btn.setGeometry(140, 330, 70, 30)
        self.textBrowser.setGeometry(40, 80, 400, 240)
        self.btn_1.setGeometry(240, 330, 70, 30)
        # 退出按钮设置
        # self.btn_1.clicked.connect(app.quit)
        # 设置查询按钮
        self.btn.clicked.connect(self.show_weather_info)
        self.show()

    def query_weather_info(self, code):
        html = f'http://wthrcdn.etouch.cn/weather_mini?citykey={code}'
        info = requests.get(html)
        info.encoding = 'utf-8'
        info_json = info.json()
        return info_json

    def show_weather_info(self):
        city_name = self.lineEdit.text()
        city_id = self.name_id_dict.get(city_name)
        if city_id is None:
            self.textBrowser.clear()
            self.textBrowser.append("未查到...... \n老哥，检查一下城市名字")
        else:
            print(city_name + ":" + city_id)
            info = self.query_weather_info(city_id)
            print(info)
            self.textBrowser.clear()
            list_info = self.conver_weather_info(info)
            for data in list_info:
                self.textBrowser.append(data)
        self.lineEdit.clear()

    def conver_weather_info(self, info_json):
        data = info_json['data']
        city = f"城市：{data['city']}\n"
        today = data['forecast'][0]
        date = f"日期：{today['date']}\n"
        now = f"实时温度：{data['wendu']}度\n"
        temperature = f"温度：{today['high']} {today['low']}\n"
        fengxiang = f"风向：{today['fengxiang']}\n"
        type = f"天气：{today['type']}\n"
        tips = f"贴士：{data['ganmao']}\n"
        list2 = list()
        list2.append(city)
        # list2.append(today)
        list2.append(date)
        list2.append(temperature)
        list2.append(fengxiang)
        list2.append(type)
        list2.append(tips)
        return list2

    def keyPressEvent(self, e):
        # 设置快捷键
        if e.key() == Qt.Key_Return:
            self.show_weather_info()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = my_ui()
#     ui.btn_1.clicked.connect(app.quit)
#     sys.exit(app.exec_())

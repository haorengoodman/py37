# 1. 先导入相关的库和方法
import smtplib
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart


class SendMail(object):
    def __init__(self, username, passwd, recv, title, content, file=None, img_file=None, email_host='smtp.163.com', port=25):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port
        self.img_file = img_file

    def send_mail(self):
        msg = MIMEMultipart()
        # 附件普通文件
        if self.file:  # 处理附件的
            att = MIMEText(open(self.file, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % self.file
            msg.attach(att)
        # 附件图片(2进制文件)
        if self.img_file:
            image_data = open(self.img_file, 'rb')
            message_image = MIMEImage(image_data.read())
            image_data.close()
            msg.attach(message_image)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = self.recv  # 接收者账号列表
        self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')

    def __del__(self):
        self.smtp.quit()


if __name__ == '__main__':
    m = SendMail(
        username='haorengoodman@163.com',
        passwd='qaz123WSX',
        recv='gaotao@news.cn',
        title='测试邮件',
        content='monitor',
        file='D:\\myDoc\\a-doc\\ooxx.xlsx',
        img_file="E:\\data\\3707078753@chatroom_1463719220004_930.gif"
    )
    m.send_mail()

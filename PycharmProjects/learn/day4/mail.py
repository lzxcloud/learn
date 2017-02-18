#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mailsender():
    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["lzx", '755320727@qq.com'])
    msg['To'] = formataddr(["zhangyuguang", 'zhangyuguang@live.com'])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.qq.com", 25)
    server.login("755320727", "PM1@gdm.")
    server.sendmail('755320727@qq.com', ['755320727@qq.com', ], msg.as_string())
    server.quit()
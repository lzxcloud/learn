#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('hello lzx', 'plain', 'utf-8')
msg['From'] = formataddr(["zhangyugaung", 'lzxcloud@126.com'])
msg['To'] = formataddr(["lzx", '755320727qq.com'])
msg['Subject'] = "主题"

server = smtplib.SMTP("smtp.126.com", 25)
server.login("lzxcloud@126.com", "a755320727")
server.sendmail('lzxcloud@126.com', ['755320727@qq.com', ], msg.as_string())
server.quit()
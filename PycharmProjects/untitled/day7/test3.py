import smtplib
import  getpass
from email.mime.text import MIMEText
from email.utils import formataddr
#text 是邮件内容  sname = 发信人名字 smail = 发信人邮件  spassword 是 发信人邮件密码 rmail 是收件人邮箱地址 rname收件人名字
# theme 是主题

text = "test send mail"
sname = "发件人名字"
smail = "发信人邮件地址"
theme = "hellow"
rmail = "收件人邮件地址"
rname = "收件人名字"
spassw =getpass.getpass("请输入密码")

def sendmail(text,sname,smail,theme,rmail,rname):
    spassw = getpass.getpass("请输入密码")
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = formataddr([sname, smail])
    msg['To'] = formataddr([rname, rmail])
    msg['Subject'] = theme
    #邮件smtp服务器地址 根据需求修改
    server = smtplib.SMTP("smtp.126.com", 25)
    server.login(smail, spassw)
    server.sendmail(smail, [rmail, ], msg.as_string())
    server.quit()


sendmail(text,sname,smail,theme,rmail,rname)
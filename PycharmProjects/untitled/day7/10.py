#!/usr/bin/env python
import  getpass
username= input("请输入用户名")
password=getpass.getpass("请输入用户名")
if username == "" and password == "123456":
    print("登录成功 ")
else:print("登录失败")
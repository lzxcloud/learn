#!/usr/bin/env python
#应用 根据用户输入内容导入模块
mo =  input('请输入模块名称')

dd = __import__(mo)
r = dd.F1()
print(r)

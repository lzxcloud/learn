#!/usr/bin/env python3
import  requests
#发送请求
rep = requests.get('http://www.liuxing999.com/mindex.php',)
print(rep.text)
#获取内容
#获取其他url
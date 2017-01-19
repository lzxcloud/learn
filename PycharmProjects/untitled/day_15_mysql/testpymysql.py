#!/usr/bin/env python3
# 创建连接
import pymysql
conn = pymysql.connect(host='192.168.0.99', port=3306, user='root', passwd='123456', db='userinfo')
# 创建游标 游标作用就是用来存储数据的
cursor = conn.cursor()
cursor.execute("select * from tb1;")
row_1 = cursor.fetchone()
print(row_1)


cursor.close()

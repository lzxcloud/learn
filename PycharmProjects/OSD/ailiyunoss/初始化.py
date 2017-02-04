#!/usr/bin/env python3
import oss2
auth = oss2.Auth('您的AccessKeyId', '您的AccessKeySecret')
endpoint = 'http://oss-cn-hangzhou.aliyuncs.com' # 假设Bucket处于杭州区域
service = oss2.Service(auth, 'http://oss-cn-hangzhou.aliyuncs.com', connect_timeout=3600) #设置一个超时时间 s为单位
bucket = oss2.Bucket(auth, endpoint, '您的Bucket名') #根据创建名创建一个对象

#以后程序需要添加
bucket.put_object_from_file('img2.png', 'p2.png') #(两个参数)

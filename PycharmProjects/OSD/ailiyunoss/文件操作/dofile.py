#!/usr/bin/env python3
import oss2
auth = oss2.Auth("LTAI5qBxauyWc9P8", "hKuhmNPWo11AdPRSynoMZsqfHepsIu")
endpoint = 'oss-cn-shanghai.aliyuncs.com'
service = oss2.Service(auth, 'http://oss-cn-shanghai.aliyuncs.com')
bucket = oss2.Bucket(auth, endpoint, "pub-lzx")

#上传文件
#bucket.put_object('remote.txt', 'hellow oss')
#或者按照b上传
# bucket.delete_object('remote.txt') #删除文件
# bucket.put_object('remote.txt', b'hellow oss')
# 指定编码
# bucket.put_object('remote.txt', u'content of object') remote.txt 是在bucket中的名字
# 事实上，oss2.Bucket.put_object的第二个参数（参数名为data）可以接受两种类型的字符串：
#
# bytes：直接上传
# unicode：会自动转换为UTF-8编码的bytes进行上传




#上传本地文件
#方法一
# with open("p1.png","rb") as f:
#     bucket.put_object('img1.png', "f")

#方法二 更方便一些
bucket.put_object_from_file('img2.png', 'p2.png') #(两个参数)



#返回值
result = bucket.put_object('remote2.txt', 'balalbala') #返回的是一个对象

print(result)
print('http status: {0}'.format(result.status))
print('request_id: {0}'.format(result.request_id))
print('ETag: {0}'.format(result.etag))
print('date: {0}'.format(result.headers['date']))
# 每个OSS服务器返回的响应都有共同属性：
#
# status：HTTP返回码
# request_id：请求ID
# headers：HTTP响应头部
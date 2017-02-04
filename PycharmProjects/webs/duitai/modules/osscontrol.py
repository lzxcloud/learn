#!/usr/bin/env python3
import oss2
auth = oss2.Auth("LTAI5qBxauyWc9P8", "hKuhmNPWo11AdPRSynoMZsqfHepsIu")
endpoint = 'oss-cn-shanghai.aliyuncs.com'
service = oss2.Service(auth, 'http://oss-cn-shanghai.aliyuncs.com')
bucket = oss2.Bucket(auth, endpoint, "pub-lzx")


def upfile(name,obj):
    bucket.put_object(name, obj)

def dropfile():
    pass
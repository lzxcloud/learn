#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import base64
import os
import oss2
auth = oss2.Auth("LTAI5qBxauyWc9P8", "hKuhmNPWo11AdPRSynoMZsqfHepsIu")
endpoint = 'oss-cn-shanghai.aliyuncs.com'
bucket = oss2.Bucket(auth, endpoint, "pub-lzx")
# 准备回调参数
callback_dict = {}
callback_dict['callbackUrl'] = 'oss-cn-shanghai.aliyuncs.com:23450'
callback_dict['callbackHost'] = 'oss-cn-shanghai.aliyuncs.com.com'
callback_dict['callbackBody'] = 'filename=${object}&size=${size}&mimeType=${mimeType}'
callback_dict['callbackBodyType'] = 'application/x-www-form-urlencoded'
# 回调参数是json格式，并且需要base64编码
callback_param = json.dumps(callback_dict).strip()

base64_callback_body = base64.b64encode(callback_param)
# 回调参数编码后放在header中传给oss
headers = {'x-oss-callback': base64_callback_body}
# 上传并回调
result = bucket.put_object('story.txt', 'a'*1024*1024, headers)
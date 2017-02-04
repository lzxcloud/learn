#!/usr/bin/env python3

import oss2
auth = oss2.Auth("LTAI5qBxauyWc9P8", "hKuhmNPWo11AdPRSynoMZsqfHepsIu")
# service = oss2.Service(auth, 'oss-cn-shanghai.aliyuncs.com')
endpoint = 'oss-cn-beijing.aliyuncs.com' # 假设Bucket处于北京
endpoint_hd="oss-cn-shanghai.aliyuncs.com"
#查看所有的Bucket
# print([b.name for b in oss2.BucketIterator(service)])


#创建一个Bucket
# bucket = oss2.Bucket(auth,endpoint,"lzx-text") #创建一个北京节点的Bucket
# bucket.create_bucket(oss2.BUCKET_ACL_PRIVATE) #为这个Bucket设置权限
bucket_hd= oss2.Bucket(auth,endpoint_hd,"pub-lzx")

#删除一个Bucket
#
# try:
#     bucket.delete_bucket()
# except oss2.exceptions.BucketNotEmpty:
#     print('bucket is not empty.')
# except oss2.exceptions.NoSuchBucket:
#     print('bucket does not exist')



#查看Bucket访问权限

print(bucket_hd.get_bucket_acl().acl)
#
# 设置Bucket访问权限
#
# 把Bucket的访问权限设为私有：
#
# bucket.put_bucket_acl(oss2.BUCKET_ACL_PRIVATE)
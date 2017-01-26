#!/usr/bin/env python3

import oss2
auth = oss2.Auth("LTAI5qBxauyWc9P8", "hKuhmNPWo11AdPRSynoMZsqfHepsIu")
service = oss2.Service(auth, 'oss-cn-shanghai.aliyuncs.com')

print([b.name for b in oss2.BucketIterator(service)])
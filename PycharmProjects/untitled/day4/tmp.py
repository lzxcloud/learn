#!/usr/bin/env python
#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
for i in dic:
    if len(dic[i])>2:
        print(dic[i][0:2])
    else:print(dic[i])

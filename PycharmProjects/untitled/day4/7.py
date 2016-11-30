#!/usr/bin/env python
#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
def funcl(s):
    new_tmp=[]
    if type(s) is dict:
        for i in dic:
            if len(dic[i]) > 2:
                new_tmp.append(dic[i][0:2])
            else:
                new_tmp.append(dic[i])
        return new_tmp
    else:return "type error"
r = funcl({"k1": "v1v1", "k2": [11,22,33,44]})
print(r)
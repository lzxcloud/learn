#!/usr/bin/env python
#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def funcl(s):
    if type(s) is list:
        if len(s) >2:
            return s[0:2]
        else:return s[:]
    else:return "TYPE ERROR!!"
print(funcl([11,232,23232,"2323"]))
#!/usr/bin/env python
#写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
def funcl(s):
    new_tmp=[]
    if type(s) is (list or tuple):
        for i,j in enumerate(s):
            if i % 2 != 0:
                new_tmp.append(j)
            else:pass
    else:return "type error"
    return new_tmp
r=funcl(["sds",2323,11,"2323"])
print(r)
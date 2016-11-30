#!/usr/bin/env python
#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def funcl(s):
    if type(s) is (str or list or tuple):
        if len(s) > 5:
            return "大于5"
        else:return "不大于5"
    else:return "TYPE ERROR!!"
print("判断长度是不是大于5")
# r = funcl(input("请输入字符串、列表、元组")) 该方式作废 因为input会返回一个str 就不能判定是不是字符串、列表、元组
print(funcl("tests"))
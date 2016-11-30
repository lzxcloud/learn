#!/usr/bin/env python
#写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def funcl(s):
    al_num = 0
    spance_num = 0
    digit_num = 0
    others_num = 0
    for i in range(len(s)):
        if s[i].isdigit():
            digit_num += 1
        elif s[i].isspace():
            spance_num += 1
        elif s[i].isalpha():
            al_num += 1
        else:
            others_num += 1
    return (digit_num,al_num,spance_num,others_num)
r = funcl(input("请输入一个字符串"))
print("输入的字符串中:\n【数字】、【字母】、【空格] 以及 【其他】的个数分别是")
print(r)
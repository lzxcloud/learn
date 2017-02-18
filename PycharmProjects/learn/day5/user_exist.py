#!/usr/bin/env python
#-*- coding: utf-8 -*-
def user_exist(user):
    """
    #用于检测用户是否存在
    :param user:#要检查的用户名
    :return:
    """
    lens = len(user)
    num = 0
    Token=False
    with open('db.txt','r',encoding='utf-8')as f:
        for line  in  f:
            line = line.strip()
            a=line[0:lens]
            print(a)
            if line[0:lens] == user:
                Token = True
                break
            else:continue
        if Token == False:
            return False
        else:return True
    return num
print(user_exist('mikunote'))
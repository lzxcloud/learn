#!/usr/bin/env python
def login():
    """
    #用于用户名和密码的验证
    :param user:
    :param password:
    :return:
    """
    user = input("请输入用户名")
    password=input("请输入密码")
    lens = len(user)
    Token=False
    with open('db.txt','r+',encoding='utf-8') as f:
        for line in f:
            line= line.strip()
            if line == user + password:
                Token = True
            else:Token=False
            continue
        if Token == True:
            return 'ok welcome'
        elif Token == False:
            return 'nonono'

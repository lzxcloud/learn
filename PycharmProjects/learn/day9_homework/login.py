#!/usr/bin/env python3
import sys
from day9_homework import admin
from day9_homework import users


def UserLogin(username, password):
    """
    #用于用户名和密码的验证
    :param user:
    :param password:
    :return:
    """
    # user = input("请输入用户名")
    # password = input("请输入密码")
    lens = len(username)
    Token = False  # 条件令牌
    with open('db.txt', 'r', encoding='utf-8') as f:
        # 循环遍历文件 符合条件把Token令牌置为Ture
        for line in f:
            line = line.strip()
            if (line[0:lens] == username) and (line[lens+1:] == password):
                Token = True
            else:
                continue
        if Token == True:
            print('欢迎 ' + username)
        elif Token == False:
            print('用户名或者密码错误')
            sys.exit()


def login():
    """
    #用于登陆验证
    :return:
    """
    print('---------欢迎登陆选课系统---------')
    role = input('请选择角色(序号)\n1----教师    2----学生    3----管理员\n')
    print('您选择的角色(序号)为' + role)
    user = input("请输入用户名")
    password = input('请输入密码')

    if role == '1':
        UserLogin(user, password)
        users.Teacher.Main(user)
    elif role == '2':
        UserLogin(user, password)
        username = users.Student(user, '男')
        # srta = '{}.Main({})'.format(username, username)
        # eval(str(srta))
        S_Name = str(user)
        username.Main(S_Name)
    elif role == '3':
        a = admin.Admin('admin', '123456')
        if user == 'admin' and password == '123456':
            a.Main()
        else:
            print('用户名或密码错误')
    else:
        print('输入有误请重新输入')

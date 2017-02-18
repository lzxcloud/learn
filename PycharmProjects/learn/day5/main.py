#!/usr/bin/env python
#-*- coding: utf-8 -*
import os
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
    Token=False#条件令牌
    with open('db.txt','r+',encoding='utf-8') as f:
        #循环遍历文件 符合条件把Token令牌置为Ture
        for line in f:
            line= line.strip()
            if line == user + ':'+password:
                Token = True
            else:Token=False
            continue
        if Token == True:
            return '欢迎 '+ user
        elif Token == False:
            return 'nonono'
def register():
    """
    #用于用户注册
    :param username:
    :param password:
    :return:
    """
    user = input("请输入用户名")

    if user_exist(user) == True:
        return "用户已经存在"
    password = input("请输入密码")
    password2=input("请再输入密码")
    if password == password2:
        with open('db.txt', 'a', encoding='utf-8')as f:
            temp="\n" + user + ':' + password
            f.write(temp)
            return "注册成功！！！"
    else:
        return "密码不一致请重新输入"
        register()
def user_exist(user):
    """
    #用于检测用户是否存在
    :param user:#要检查的用户名
    :return:
    """
    lens = len(user)
    Token=False#条件令牌
    with open('db.txt','r',encoding='utf-8')as f:
        # 循环遍历文件 符合条件把Token令牌置为Ture
        for line in f:
            line = line.strip()
            if line[0:lens] == user:
                Token = True
                break
            else:continue
        if Token == False:
            return False
        else:return True
def user_del(user):
    """
    #该功能只能在linux平台运行
    :param user: 要删除的用户名
    :return:
    """
    command = 'sed -i \'/' + user + '/d\' db.txt'
    os.popen(command)
def main():
    print("欢迎登录xxx系统")
    print("请选择功能")
    inp=input("1:登录     2注册     3用户管理\n")
    if inp == '1':
        print(login())
    elif inp == '2':
        print(register())
    elif inp == '3':
        print('数据库中已有的用户有')
        with open('db.txt', 'r') as f:
            for lines  in f:
                lines=lines.strip()
                lines_list=lines.split(':')
                print(lines)
        user_del(input('请输入要删除的用户名(只能在linux中运行)\n'))
        print('执行完成')
        with open('db.txt', 'r') as f:
            for lines in f:
                lines = lines.strip()

                print(lines)
main()

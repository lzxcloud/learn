#!/usr/bin/env python3
import pickle
from day9_homework import users
from day9_homework import Course

st = True

class Admin:
    def __init__(self, username, password):
        self.name = username
        self.password = password

    def SaveInfo(self, name, info):
        filename = '{}info'.format(name)
        with open('./admin/'+filename, 'wb+') as fp:
            fp.write(pickle.dumps(info))
            fp.flush()

    def User(self):
        pass

    def Main(self):
        print('登陆成功')
        print('1 创建老师    2 创建课程    3退出')
        cmd = input('请选择功能' + '\n')
        if cmd == '1':
            T_Name = input('请输入教师姓名')
            age = input('请输入教师年龄')
            sex = input('请输入教师性别')
            T_Name = users.Teacher(name=T_Name, age=age, sex=sex)
            info = eval('T_Name.ReturnInfo()')
            self.SaveInfo(info[0], info)
        elif cmd == '2':
            C_Name = input('请输入课程名称')
            time = input('请输入课程时长(分钟)')
            cost = input('请输入课程花费(元)')
            teacher = input('请输入教师名称')
            C_Name = Course(name=C_Name, time=time, cost=cost, teacher=teacher)
            eval('C_Name.AddList()')
        elif cmd == '3':
            pass
        else:
            print('输入错误')


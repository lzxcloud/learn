#!/usr/bin/env python3
import pickle
from day9_homework import Course


class Teacher:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__asset = 0
        self.sex = sex

    def AddAsset(self, moeny):
        self.__asset += moeny

    def ReturnInfo(self):
        TeacherInfoList = [self.name, self.age, self.sex, self.__asset, ]
        return TeacherInfoList

    @staticmethod
    def Main(name):
        print('您的工资为:')
        filename = '{}info'.format(name)
        with open('./admin/'+filename, 'rb') as f:
           info = pickle.loads(f.read())
        print(info[3])


class Student:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.course_list = []

    def DisCourseList(self, start, end, flag):
        with open('./admin/CourseInfo', 'r') as f:
            if flag == 1:
                for line, j in enumerate(f.readlines()[start:end]):
                    print(line, j)
            else:
                for line, j in enumerate(f.readlines()[start:end]):
                    return line, j


    def Choose(self, Choose_C):
        if Choose_C == '1':
            C_List = pickle.dumps(eval(self.DisCourseList(1, 2, 2)[1]))
            C_name = pickle.loads(C_List)
            self.course_list.append(C_name[0])
        elif Choose_C == '2':
            C_List = pickle.dumps(eval(self.DisCourseList(2, 3, 2)[1]))
            C_name = pickle.loads(C_List)
            self.course_list.append(C_name[0])
        elif Choose_C == '3':
            C_List = pickle.dumps(eval(self.DisCourseList(3, 4, 2)[1]))
            C_name = pickle.loads(C_List)
            self.course_list.append(C_name[0])

    def SaveInfo(self, name):
        filename = '{}info'.format(name)
        with open('./students/'+filename, 'wb+') as f:
            f.write(pickle.dumps(self.course_list))

    def ReadInfo(self, name):
        filename = '{}info'.format(name)
        with open('./students/' + filename, 'rb') as f:
            info = pickle.loads(f.read())
            return info

    def Main(self, name):
        cmd = input('请选择功能\n1选课     2显示以选课程     3上课\n')
        if cmd == '1':
            flag = False
            while flag == False:
                self.DisCourseList(0, 4, 1)
                cmd = input('请输入选择课程的编号')
                self.Choose(cmd)
                self.SaveInfo(name)
                cmd2 = input('是否退出 (Y/N)')
                str.capitalize(cmd2)
                if cmd2 == 'Y':
                    flag = True
        elif cmd == '2':
            print('您已选课程如下:\n')
            print(self.ReadInfo(name))
        elif cmd == '3':
            print('该功能尚未完善,敬请期待')
        else:
            print('输入参数有误,请重试')


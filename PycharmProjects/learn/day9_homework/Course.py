#!/usr/bin/env python3


class Course:
    def __init__(self, name, time, cost, teacher):
        self.name = name
        self.time = time
        self.cost = cost
        self.teacher = teacher

    def AddList(self):
        CourseList = [self.name, self.time, self.cost, self.teacher]
        with open('./admin/CourseInfo', 'a+',) as fp:
            fp.write(str(CourseList)+'\n')
            fp.flush()



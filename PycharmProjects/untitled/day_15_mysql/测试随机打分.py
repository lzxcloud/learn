#!/usr/bin/env python3
while True:
    import random,math
    y_ps = int(input("请输入原来的平时成绩"))
    y_ps = y_ps * 3
    f_num = y_ps * 0.4
    m_num = math.ceil(y_ps * 0.36)
    e_num = math.ceil(y_ps * 0.24)

    print(f_num,m_num,e_num)

#!/usr/bin/env python3


def formatdic(dic_info):
    """
    #用于将字典格式化并打印
    :param dic_info:含有3个字典和一个城市名称的tuple
    :return:
    """
    print('今天详细天气预报：')
    li = ['日期&天气', '温度', '风力']
    print(dic_info[0]['省份'], dic_info[0]['城市'])
    str_date = '{}{:>20}{:>}'.format(dic_info[0]['日期&时间'], dic_info[0]['日期&天气'], dic_info[0]['温度'])
    print(str_date)
    print(dic_info[0]['天气预报'])
    #格式化并打印内容
    for i, j in enumerate(li):
        if i == 1:
            str_date = '{}\t{:>28}'.format(dic_info[1][j], dic_info[2][j])
        elif i == 2:
            str_date = '{}\t{:>24}'.format(dic_info[1][j], dic_info[2][j])
        else:
            str_date = '{}\t{:>20}'.format(dic_info[1][j], dic_info[2][j])
        print(str_date)



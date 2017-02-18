#!/usr/bin/env python3
from xml.etree import ElementTree as ET


def readerxml():
    """
    #接收原始xml内容，并格式化成一个列表返回
    :param info:
    :return:
    """
    li_info = []
    tree = ET.parse('data.xml')
    root = tree.getroot()
    #清xml无用内容
    for child in root:
        if '.' in child.text:
            continue
        elif child.text.isdigit():
            continue
        else:
            li_info.append(child.text)
    return li_info


def wetherformat(li_info):
    """
    #用于接收 已经格式化的 xml信息 并转换成字典返回
    :param li_info: # 列表
    :return:
    """
    dic_info_day1 = {}
    dic_info_day2 = {}
    dic_info_day3 = {}
    li_name = ['省份', '城市', '日期&时间', '温度', '日期&天气', '风力', '天气预报', '紫外线']
    li_name_day_after = ['温度', '日期&天气', '风力']
    # 将列表里的信息 添加到字典中去
    for i in range(0, 7):
        dic_info_day1[li_name[i]] = li_info[i]
    l = 0
    for i in range(8, 11):
        dic_info_day2[li_name_day_after[l]] = li_info[i]
        l += 1
    l = 0
    for i in range(11, len(li_info)):
        dic_info_day3[li_name_day_after[l]] = li_info[i]
        l += 1
    return dic_info_day1, dic_info_day2, dic_info_day3,li_info[1]


#!/usr/bin/env python3
import requests

def getwebinfo(city):
    """
    #从网站获取字符串，并写入一个名为data的xml文件
    :param city:
    :return:
    """
    url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=' + city
    ret = requests.get(url)
    info = ret.text
    #创建data.xml文件
    with open('data.xml', 'w') as f:
        f.write(info)
        f.flush()
        f.close()

#!/usr/bin/env python3
from day8_homework.weatherchecker import getwebinfo
from day8_homework.weatherchecker import checkweather
from day8_homework.weatherchecker.xmlreader import readerxml, wetherformat


city = input('请输入想要查询的城市名称 ps：有些城市可能没有 （╯－＿－）╯╧╧''\n')
getwebinfo.getwebinfo(city)
checkweather.formatdic(wetherformat(readerxml()))

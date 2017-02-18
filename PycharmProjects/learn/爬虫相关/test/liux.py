#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import time
import hashlib
import re




def login():
    login_dict = {
        'username': "mikunote",
        'password': "",
        'imgcode': "",
        'f': 'json'
    }

    login_res = requests.post(
        url="http://www.liuxing999.com/mindex.php",
        data=login_dict,
        #来源url
        headers={'Referer': 'http://www.liuxing999.com/?p=login'})

    # 登陆成功之后获取服务器响应的cookie

    resp_cookies_dict = login_res.cookies.get_dict()


    rep = requests.get("www.liuxing999.com/?p=online")
    # 登陆成功后，获取服务器响应的内容
    resp_text = login_res.text
    print(rep.text)

    print(resp_cookies_dict)


login()


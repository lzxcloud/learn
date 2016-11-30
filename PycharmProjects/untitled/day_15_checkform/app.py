#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import re
class MainForm(object):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.port = "(\d+)"
        self.phone = "^1[3|4|5|8][0-9]\d{$}$"
    def check_valid(self,handle):
        flag = True
        value_dict ={}
        for key,regular in self.__dict__.items():
            input_value = handle.get_argument(key)
            val = re.match(regular,input_value)
            print(key,input_value, val, regular)
            if not val:
                flag =False
                value_dict[key]=input_value
            return flag, value_dict

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self, *args, **kwargs):
        obj = MainForm()
        is_valid,value_dict = obj.check_valid(self)
        print(is_valid)
        if is_valid:
            print(value_dict)

settings = {
    'templates':'view',#模板路劲的配置
    'static_path': 'static',#静态文件的路径
    'static_url_prefix': '/sss/',#路劲前缀知道即可
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
],**settings)

if __name__ == "__main__":
    #socket运行起来了
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
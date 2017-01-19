#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
inputs_list=[]

class MainHandler(tornado.web.RequestHandler):
    #路由映射,路由系统
    def get(self):
        #get 获取数据
        # print(self.get_argument("name"))
        # print(self.get_argument("age"))
        # self.write("Hello, world")
        #1 打开s1.html文件 读取内容(包含特殊语法)
        #2 xxxooo=[11,22,33,44] &&读取内容(包含特殊语法)
        #3 得到新的字符串
        #4 返回给用户
        self.render("s1.html",xxxooo=inputs_list)
    def post(self, *args, **kwargs):
        name = self.get_argument("xxxx")
        inputs_list.append(name)
        self.render("s1.html", xxxooo=inputs_list)
settings = {
    'template_path':'template',#模板路劲的配置
    'static_path':'static',#静态文件的路径
    # 'static_url_prefix': '/sss/',#路劲前缀知道即可
}

application = tornado.web.Application([
    #匹配url 第一个参数接收一个列表 第二个参数是配置
    (r"/index", MainHandler),
],**settings)

if __name__ == "__main__":
    #socket运行起来了
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
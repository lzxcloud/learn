#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import time
USER_INFO = {"username": None, "info": {"is_login": False, "cookie": ""}}
inputs_list = []
NEWS_LIST = [
    {"title": "上海哔哩哔哩公司今日冠名了'上海大鲨哔'篮球队", "content": "姚老板一脸无语,心疼姚老板一1s+++++", },
]


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("index.html", user_info=USER_INFO)
#     def post(self, *args, **kwargs):
#


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        # self.render("index.html",user_info =USER_INFO)
        co = self.get_cookie("login_user")
        if co == "lzx":
            self.render("index.html", user_info=USER_INFO, list_info=inputs_list)
        else:
            self.render("index.html", user_info=USER_INFO, list_info=inputs_list)
    def post(self, *args, **kwargs):
        if self.get_cookie("login_user") == "lzx":
            name = self.get_argument("xxxx")
            inputs_list.append(name)
            self.render("index.html", user_info=USER_INFO, list_info=inputs_list)
        else:
            self.render("index.html", state="show",list_info=inputs_list)


class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        passwd = self.get_argument("pwd", None)
        checked = self.get_argument("auto",None)
        if username == "lzx" and passwd == "lzxcloud":
            if checked:
                USER_INFO["username"] = username
                USER_INFO["info"]["is_login"] = True
                self.set_cookie('login_user', username, expires_days=7)
            else:
                r = time.time() + 10
                self.set_cookie('username', self.get_argument("username"), expires=r)

            # self.render("index.html", user_info=USER_INFO, list_info=inputs_list)
            self.redirect('/index')
        else:
            self.redirect("/login")
        print(USER_INFO,username,passwd,checked)


class PubHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        if USER_INFO["is_login"]:
            title = self.get_argument("title", None)
            content = self.get_argument("news-text", None)
            temp = {"title": title, "content": content}
            NEWS_LIST.append(temp)
            self.render("index.html", user_info=USER_INFO, news_list=NEWS_LIST)
            self.redirect("/index")



settings = {
    'template_path':'template',#模板路劲的配置
    'static_path': 'static',#静态文件的路径
    # 'static_url_prefix': '/sss/',#路劲前缀知道即可
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/Publish", PubHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
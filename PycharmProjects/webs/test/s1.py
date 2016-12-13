#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import time
import json
USER_INFO = {"username": None, "info": {"cookie": ""}}
NEWS_LIST = [
    {"title": "上海哔哩哔哩公司今日冠名了'上海大鲨哔'篮球队", "content": "姚老板一脸无语,心疼姚老板一1s+++++", },
]


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("index.html", user_info=USER_INFO)
#     def post(self, *args, **kwargs):
#


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("login_user")


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        login_user = self.current_user
        if login_user:
            self.render("index.html", username=login_user ,state=True, news_list=NEWS_LIST)
        else:
            self.render("index.html",  state = False ,news_list=NEWS_LIST)


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html", state=False, news_list=NEWS_LIST)


    def post(self, *args, **kwargs):
        username = self.get_argument("username", None)
        passwd = self.get_argument("passwd", None)
        checked = self.get_argument("auto",None)
        dic = {"status":True,"messsage":""}

        print(username,passwd,checked)
        if username == "lzx" and passwd =="lzxcloud":
            USER_INFO["username"] = username
            if checked:
                self.set_secure_cookie("login_user", username, expires_days=7)
            else:
                r = time.time() + 10
                self.set_cookie("login_user",username, expires=r)
        else:
            dic["status"] = False
            dic["messsage"]="用户名或者密码错误"
        self.write(json.dumps(dic))



class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("login_user")
        self.redirect("/index")
    def post(self, *args, **kwargs):
        pass


class PubHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        title = self.get_argument("title",None)
        content = self.get_argument("news-text",None)
        temp = {"title": title, "content": content}
        NEWS_LIST.append(temp)
        self.redirect("/index")


settings = {
    "template_path": "templates",
    "static_path": "static",
    "cookie_secret": "blog.lzxcloud.com",
    "login_url":"/login"
}
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/Publish", PubHandler),

], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
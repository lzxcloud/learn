#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import time

user_info= {"username":"","is_login":False}
class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')

class ManagerHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        co = self.get_cookie('username')
        if co == user_info["username"]:
            self.render('manager.html')
        else:
            self.redirect("/login")

class LogoutHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.cl
        self.redirect('/login')
class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html',  status_text="")

    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        check = self.get_argument('auto', None)
        if username == 'alex' and pwd == "sb":

            if check:
                user_info["username"] = username
                self.set_cookie('username', self.get_argument("username"), expires_days=7)
            else:
                r = time.time() + 10
                self.set_cookie('username',self.get_argument("username"), expires=r)
            self.redirect('/manager')
        else:
            self.render('login.html', status_text="登录失败")

settings = {
    'template_path': 'views', # 模板路径的配置
    'cookie_secret': 'sdfgsdfg'
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/manager", ManagerHandler),
    (r"/logout", LogoutHandler),
], **settings)


if __name__ == "__main__":
    # socket运行起来
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

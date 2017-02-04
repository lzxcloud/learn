#!/usr/bin/env python3
import tornado.ioloop
import tornado.web
from controllers import admin
from controllers import search
settings = {
    'template_path': "../templates",
    "static_path": "../static",
}

application = tornado.web.Application([
    (r"/index", search.IndexHandler),
    (r"/admin",admin.AdminHandler)
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

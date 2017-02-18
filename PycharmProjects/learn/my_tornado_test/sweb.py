#!/usr/bin/env python3

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self, *args, **kwargs):
        vara = self.get_argument("aa")
        print(vara)
settings = {
    "template_path":"templates",
    "static_path":"static",
    "static_url_prefix":"/static/",
}
application = tornado.web.Application([
    (r"/index", MainHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
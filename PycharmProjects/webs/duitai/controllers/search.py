#!/usr/bin/env python3
import tornado.web
from modules import osscontrol
import hashlib
from modules import duita_orm as ORM
from sqlalchemy import and_, or_


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self, *args, **kwargs):
        Stxt = self.get_argument("txt")
        hash = hashlib.md5()
        hash.update(bytes(Stxt, encoding='utf-8'))
        Ctxt = hash.hexdigest()
        conn = ORM.session()
        ret =conn.query(ORM.Img).filter_by(hexname = Ctxt).first()
        print(ret.path)

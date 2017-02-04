#!/usr/bin/env python3
import tornado.ioloop
import tornado.web
from modules import osscontrol
import hashlib
from modules import duita_orm as ORM
from sqlalchemy import and_, or_



class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin.html')

    def post(self, *args, **kwargs):
        filename = self.get_argument("filename")
        file_metas = self.request.files["fff"]
        tig1 = self.get_argument("tig1")
        tig2 = self.get_argument("tig2")
        tig3 = self.get_argument("tig3")
        hash = hashlib.md5()

        for meta in file_metas:
            file_name = meta['filename']
            kzm = file_name[int(str.find(file_name, ".")):]
            hash.update(bytes(filename, encoding='utf-8'))
            filename = hash.hexdigest()
            files=filename+kzm
            osscontrol.upfile(files, meta["body"])
            conn = ORM.session()
            put_info = ORM.Img(hexname=filename,tig1=tig1,tig2=tig2,tig3=tig3,path="http://pub-lzx.oss-cn-shanghai.aliyuncs.com/"+files)
            conn.add(put_info)
            conn.commit()
            # with open(filename,'wb') as up:
            #     up.write(meta['body'])


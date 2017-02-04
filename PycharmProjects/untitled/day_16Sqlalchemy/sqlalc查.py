#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
engine = create_engine("mysql+pymysql://root:123456@192.168.0.99:3306/duita?charset=utf8")

Base = declarative_base()#生成一个SQLORM基类


class Img(Base):
    __tablename__ = 'img'
    id = Column(Integer, primary_key=True,autoincrement=True)
    hexname = Column(String(40),index=True)
    tig1 = Column(String(10),default=None)
    tig2 = Column(String(10),default=None)
    tig3 = Column(String(10),default=None)
    path = Column(String(80))

    def __repr__(self):
        return "(id='%s', hexname='%s', tig1='%s', tig2='%s', tig3='%s',path='%s')" % (self.id, self.hexname, self.tig1,self.tig2,self.tig3,self.path)
Session = sessionmaker(bind=engine)
session = Session()
# ret = session.query(Img).all()

# ret = session.query(User.name, User.extra).all()
ret = session.query(Img).filter_by(hexname='4ad69a1d98ef958c0d0592f02e523611').first()
print(ret.path)

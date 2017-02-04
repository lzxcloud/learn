#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:123456@192.168.0.99:3306/duita?charset=utf8")
#解决存储到数据库中文乱码的问题

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
def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def session():
    cls = sessionmaker(bind=engine)
    return cls()
init_db()
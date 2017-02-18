#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
print(sqlalchemy.__version__)


engine = create_engine("mysql+pymysql://root:123456@192.168.0.99:3306/userinfo")

Base = declarative_base()#生成一个SQLORM基类

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20),index=True)
    fullname = Column(String(20),unique=True)
    password = Column(String(20))

ed_user = User(name='alex', fullname='Liu jie', password='123')
# 1.1.4
# <__main__.User object at 0x1021326a0>


# #这两行触发sessionmaker类下的__call__方法，return得到 Session实例，赋给变量session，所以session可以调用Session类下的add，add_all等方法
MySession = sessionmaker(bind=engine) #创建session的实例对象
session = MySession()
#
session.add(ed_user)#将数据添加进去，数据库插入动作
session.commit()

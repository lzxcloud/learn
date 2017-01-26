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
MySession = sessionmaker(bind=engine) #创建session的实例对象
session = MySession()

ret = session.query(User).all()
# ret = session.query(User.name, User.extra).all()
# ret = session.query(User).filter_by(name='alex').all()
# ret = session.query(User).filter_by(name='alex').first()
print(ret.name)

#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:123456@192.168.0.99:3306/userinfo")

Base = declarative_base()#生成一个SQLORM基类

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20),index=True)
    fullname = Column(String(20),unique=True)
    password = Column(String(20))

Base.metadata.create_all(engine)  #创建所有表结构


#创建一个对象相当于在表里插入了一条数据
ed_user = User(name='xiaoyu', fullname='Xiaoyu Liu', password='123')
print(ed_user)

# 1.1.4
# <__main__.User object at 0x1021326a0>


# #这两行触发sessionmaker类下的__call__方法，return得到 Session实例，赋给变量session，所以session可以调用Session类下的add，add_all等方法
MySession = sessionmaker(bind=engine) #创建session的实例对象
session = MySession()
#
session.add(ed_user)#将数据添加进去，数据库插入动作
# # our_user = session.query(User).filter_by(name='ed').first()
# # SELECT * FROM users WHERE name="ed" LIMIT 1;
#提交多行数据
# # session.add_all([
# #     User(name='alex', fullname='Alex Li', password='456'),
# #     User(name='alex', fullname='Alex old', password='789'),
# #     User(name='peiqi', fullname='Peiqi Wu', password='sxsxsx')])

session.commit() #对数据库进行修改的时候必须执行的操作
#查询不部分
#print(">>>",session.query(User).filter_by(name='ed').first())
#print(session.query(User).all())#查询语句
# for row in session.query(User).order_by(User.id):
#      print(row)
# for row in session.query(User).filter(User.name.in_(['alex', 'wendy', 'jack'])):＃这里的名字是完全匹配
#     print(row)
# for row in session.query(User).filter(~User.name.in_(['ed', 'wendy', 'jack'])): ~ 代表去反的意思
#     print(row)
#print(session.query(User).filter(User.name == 'ed').count())
#from sqlalchemy import and_, or_

# for row in session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')):
#     print(row)
# for row in session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')):
#     print(row)
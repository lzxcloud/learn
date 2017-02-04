#!/usr/bin/env python3
#版本检查
import sqlalchemy

print(sqlalchemy.__version__)

#连接数据库
from sqlalchemy import create_engine #连接引擎

# MySQL - Python
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

# pymysql
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

# MySQL-Connector
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

# 更多详见：http: // docs.sqlalchemy.org / en / latest / dialects / index.html

engine = create_engine("mysql+pymysql://root:123456@192.168.0.99:3306/userinfo",)

#echo=True 会将来执行的sql 记录日志
# 例如这些
# /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/lanzexi/learn/PycharmProjects/untitled/day_16Sqlalchemy/sqlc.py
# 2017-01-20 20:05:30,490 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
# 2017-01-20 20:05:30,490 INFO sqlalchemy.engine.base.Engine {}
# 2017-01-20 20:05:30,494 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
# 2017-01-20 20:05:30,494 INFO sqlalchemy.engine.base.Engine {}
# 2017-01-20 20:05:30,499 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8' and `Collation` = 'utf8_bin'
# 2017-01-20 20:05:30,500 INFO sqlalchemy.engine.base.Engine {}


#声明一个表
#使用 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句
from sqlalchemy.ext.declarative import declarative_base
#创建一个基类，之后所有表都继承这个基类
Base = declarative_base()
#创建表结构
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    password = Column(String(20))


    #创建定长的
    info =Column(chr(30))
#__repr__只是为了格式化用的
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
        self.name, self.fullname, self.password)

#执行下面这条语句，将表内容提交到数据库
Base.metadata.create_all(engine)

#创建一个实例（向表里插入一条数据)
ed_user = User(name="ed",fullname="ED Jones",password="edspassword")

#创建一个session与数据库进行连接
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)#与engine 绑定
session = Session()#创建了一个session对象

#将信息添加到数据库里面去
session.add(ed_user) #insert操作
#查询操作
ret = session.query(User).filter_by(name='ed').first()
print(ret)


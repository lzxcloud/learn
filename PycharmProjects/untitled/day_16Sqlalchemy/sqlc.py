
#!/usr/bin/env python3
#这个是内部如何处理sql语句只有当orm不好用的时候才使用这个
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@192.168.0.99:3306/userinfo",echo=True)

# 事务操作
cur = engine.execute(
    "insert into color (nid,color) values (3,'red')")
# 事务操作


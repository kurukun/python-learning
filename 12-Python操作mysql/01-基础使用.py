# 主要的新内容为连接数据库 选择数据库 获取游标对象，其他sql语句在execute内部执行即可
# 都是在表和数据库都已经创建的前提下？
from pymysql import Connection
# 构建到MySQL数据库的连接
conn = Connection(
    host='localhost',  # 主机名
    port=3306,  # 端口
    user='root',  # 用户名
    password='root'  # 密码
)

# print(conn.get_server_info())

# 获取游标对象，执行SQL语句使用该对象执行
cursor = conn.cursor()

# 选择数据库
conn.select_db('kurukun')

# 执行非查询性质的SQL语句
# cursor.execute('create table test_pyMySQL(id int);')

# 执行查询性质的sql语句
cursor.execute('select * from employee')
# 获取结果用游标.fetchall
results = cursor.fetchall()
for r in results:
    print(r)
# 与文件操作类似，使用结束后要关闭连接
conn.close()

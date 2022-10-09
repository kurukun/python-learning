from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    # autocommit=True  # 设置为True后就不需要手动提交了
)
cursor = conn.cursor()
conn.select_db('kurukun')
# 插入数据到MySQL
cursor.execute('insert into employee values(9, "0009", "舞舞舞", "女", 20, "1008612", "2022-10-9");')
# 还需要进行确认才能生效，这是手动提交，也可以自动提交
conn.commit()
# 断开连接
conn.close()

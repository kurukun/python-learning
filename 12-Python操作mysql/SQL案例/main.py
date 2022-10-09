"""
将写入到MySQL的数据通过Python代码读取出来
"""
import json

from pymysql import Connection

# 1.从数据库中读取数据并存储
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root'
)
cursor = conn.cursor()
conn.select_db('py_mysql')
cursor.execute('select * from orders')
result = cursor.fetchall()
list_result = []
for r in result:
    my_dict = {
        "date": str(r[0]),
        "order_id": r[1],
        "money": r[2],
        "province": r[3]
    }
    list_result.append(my_dict)

conn.close()
# 2.写出数据
f = open('E:/zql-Workstation/文档/output_json.txt', 'w', encoding='UTF-8')
for l in list_result:
    l = json.dumps(l, ensure_ascii=False)
    f.write(l + '\n')

f.close()

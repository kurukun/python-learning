"""
1.设计一个类，完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
"""
from data_define import Record
from file_define import FileReader, TextReader, JsonReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pymysql import Connection
# 1.数据准备部分
text_reader = TextReader('E:/zql-Workstation/文档/2011年1月销售数据.txt')
json_reader = JsonReader('E:/zql-Workstation/文档/2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_reader.read_data()
feb_data: list[Record] = json_reader.read_data()
# 合并两个月份的list
all_data = jan_data + feb_data
print(all_data)
# 需求：将数据导入到数据库中
# 构建mySQL连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    autocommit=True
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('py_mysql')
# 组织sql语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # 执行sql语句
    cursor.execute(sql)
# 关闭sql连接对象
conn.close()



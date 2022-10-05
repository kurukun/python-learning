# 导包
from pyecharts.charts import Map
# 准备地图对象
my_map = Map()
data = [
    ("北京", 99),
    ("上海", 199),
    ("湖南", 299),
    ("台湾", 399),
    ("广东", 499)
]

# 添加数据
my_map.add("测试地图", data, "china")
# 绘图
my_map.render()

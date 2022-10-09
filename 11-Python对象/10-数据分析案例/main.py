"""
1.设计一个类，完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
"""
from data_define import Record
from file_define import FileReader, TextReader, JsonReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 1.数据准备部分
text_reader = TextReader('E:/zql-Workstation/文档/2011年1月销售数据.txt')
json_reader = JsonReader('E:/zql-Workstation/文档/2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_reader.read_data()
feb_data: list[Record] = json_reader.read_data()
# 合并两个月份的list
all_data = jan_data + feb_data

# 2.开始进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 字典内已有key，则与老记录的值累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)

# 3.可视化图像
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)
bar.render('每日销售柱状图.html')


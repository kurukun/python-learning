"""
和文件相关的类定义
"""
import json

from data_define import Record


# 定义一个抽象类用于顶层设计
class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转化为record对象，将他们封装到list内返回即可"""
        pass


class TextReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件的路径

    # 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='UTF-8')
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 处理字符串的前后空格以及换行符
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


# -----------------------------------------------------------------------------------------------

class JsonReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件的路径

    # 实现抽象方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        f = open(self.path, 'r', encoding='UTF-8')
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_reader = TextReader('E:/zql-Workstation/文档/2011年1月销售数据.txt')
    json_reader = JsonReader('E:/zql-Workstation/文档/2011年2月销售数据JSON.txt')
    list1 = text_reader.read_data()
    list2 = json_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)

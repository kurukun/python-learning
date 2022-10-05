"""
文件处理相关工具
"""


def print_file_info(file_name):
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        print(f"以下为文件的全部内容\n{f.read()}")
        f.close()
    except Exception as e:
        print('出错了')


def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.close()


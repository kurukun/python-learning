# 定义字典字面量
{"zhang_san": 14, "li_si": 11}
# 定义字典变量
my_dict = {"zhang_san": 14, "li_si": 11}
print(type(my_dict))
# 空字典定义方式 1：xxx = {} 2: xxx = dict()
# Python中的key不能重复
my_dict = {"zhang_san": 14, "li_si": 11, "zhang_san": 99}
print(my_dict)  # 只保留了后面的张三
# 不能使用下标索引 但可以用key
my_dict = {"zhang_san": 14, "li_si": 11}
print(my_dict["zhang_san"])
# key和value可以是任意数据类型，但key不能是字典
# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文": 99,
        "数学": 80,
        "英语": 120
    },
    "周杰伦": {
        "语文": 91,
        "数学": 89,
        "英语": 110
    }
}
print(stu_score_dict["周杰伦"]["语文"])



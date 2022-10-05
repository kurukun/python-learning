# 新增元素
my_dict = dict()
my_dict['age'] = 14  # 若填入的key在原字典中不存在，则会新建一个key
print(my_dict)
# 更新元素
my_dict['age'] = 15  # 更新只要改value即可
print(my_dict)
# 删除元素
age = my_dict.pop('age')  # 可以用变量去接收被删除key的value
print(my_dict, age)
my_dict['num'] = 1
# 清空字典
my_dict.clear()
print(my_dict)
# 获取全部的key 字典.keys() 需要变量接收返回值 可以用来遍历字典
my_dict = {"zhang_san": 14, "li_si": 11}
keys = my_dict.keys()
print(keys)
# 遍历字典
# 方式一：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}", end='\t')
    print(f"字典的value是:{my_dict[key]}")
# 方式二：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}", end='\t')
    print(f"字典的value是:{my_dict[key]}")
# 统计字典的元素数量
num = len(my_dict)
print(num)
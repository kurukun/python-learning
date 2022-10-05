# 字符串也能通过下标索引值
value = "heima"
print(value[0])
# 字符串是一个无法修改的数据容器
# 字符串的查找
print(value.index("hei"))
# 字符串的替换
# 将字符串1替换为字符串2，不是修改字符串本身，而是得到一个新字符串
value2 = value.replace("ma", "die")
print(value2)
# 字符串的分割
# 格式：字符串.split（分隔字符串，填入的参数为分割依据），字符串本身不变，而是得到了一个列表对象
value = "hello world hello goodbye"
value2 = value.split(" ")
print(value)
print(value2)
# 字符串的规整操作 字符串.strip() 去前后空格以及换行符
value = " hello world hello goodbye "
new_value = value.strip()  # 不传入参数，去除前后空格以及换行符
print(new_value)
# 字符串.strip(字符串) 去前后指定字符串
value = "12hello world hello goodbye21"
new_value = value.strip('12')  # 传入参数，去除指定字符串，相当于把传入的字符串分成子串，满足条件的就会删除
# 统计字符串中某字符的出现次数
print(value.count("hello"))

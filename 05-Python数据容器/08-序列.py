# 内容连续 有序 可以使用下标索引的数据容器 如字符串、列表、 元组
# 格式：序列[起始位置: 结束位置: 步长] 从一个序列中取得一个子序列
# 结束下标（不含） 步长：取元素的间隔 也是创造新序列
my_list = [0, 1, 2, 3, 4, 5, 6]
# 从1开始到4结束，默认步长为1，因此步长为1时可以不写
result1 = my_list[1:5]
print(result1)
my_tuple = (0, 1, 2, 4, 5, 6)
# 起始和结束都不写表示从头开始到尾结束
result2 = my_tuple[:]
print(result2)
# 从头开始到尾结束，步长为2
my_str = "01234567"
result3 = my_str[::2]
print(result3)
# 对str进行切片，从头开始到尾结束，步长-1
my_str = "01234567"
result4 = my_str[::-1]
print(result4)
# 倒序时起始和结束位置也变成大到小
result5 = my_str[3:1:-1]
print(result5)

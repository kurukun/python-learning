# 查找某元素在列表内的下标索引（正向索引）
# 格式：列表.index(元素)
my_list = ['itheima', 'kurukun', 222]
index = my_list.index(222)
# index = my_list.index(111)
# 如果元素不存在则会报错
print(index)

# 列表的修改功能
# 格式：列表[下标]=值
my_list[0] = 'hello'
print(my_list[0])

# 插入元素
# 格式：列表.insert(下标，元素)，在指定的下标位置，插入指定的元素，原位置的元素会自动往后移
my_list.insert(1, 'tokido')
print(my_list)

# 追加元素
# 方式1——格式：append(元素)，将指定元素追加到列表尾部
my_list.append('saya')
print(my_list)
# 方式2——格式：extend(其他数据容器)，将其他数据容器的内容取出，依次追加到列表尾部
my_list2 = ['key', 'sound', 111]
my_list.extend(my_list2)
print(my_list)

# 删除指定下标索引的元素
# 方式一：del 列表[下标]
my_list = ['itheima', 'kurukun', 222]
del my_list[0]  # 只能删除不能接收被删值，后面的元素会自动往前
print(my_list)
# 方式二：列表.pop(下标)
del_elm = my_list.pop(0)  # 可以通过变量去接收这个删除值
print(my_list, del_elm)

# 删除指定元素
# 语法：列表.remove(元素)，删除某元素在列表中的第一个匹配项
my_list = ['itheima', 222, 'kurukun', 222]
my_list.remove(222)
print(my_list)

# 清空列表
my_list.clear()
print(my_list)

# 统计某元素在列表中的数量
# 列表.count(元素)
my_list = ['itheima', 222, 'kurukun', 222]
print(my_list.count(222))

# 统计列表中全部的元素数量 len()函数
print(f"列表的元素数量总共有{len(my_list)}个")


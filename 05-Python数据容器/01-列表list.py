# 定义一个列表list
my_list = ["itheima", "kuru", 666]  # 元素数据类型不限制，与js中的列表类似
print(my_list, type(my_list))
# 索引从前往后，0开始，从后往前的反向索引则是从-1开始
print(my_list[0], my_list[-1])
# 定义一个嵌套列表
my_list2 = [[1,2,3], [4, 5, 6]]
# 元素本身是列表时的索引使用方法
print(my_list2[0][-1])  # 结果是3
# 超出范围的话会报错


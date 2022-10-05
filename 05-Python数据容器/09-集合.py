# 特性：无序 不重复
# 定义集合
my_set = {"hello", "world", "kuru", "genshin", "hello"}
my_set_empty = set()  # 定义空集合
print(type(my_set_empty))
print(my_set, type(my_set))  # 结果自动去重
# 不支持下标索引访问，因为是无序的
# 添加新元素 集合.add(元素)
my_set.add("xxx")
my_set.add("kuru")
print(my_set)
# 移除新元素 集合.remove(元素)
my_set.remove("kuru")
print(my_set)
# 集合.pop() 从集合中随机取出一个元素
my_set = {"hello", "world", "kuru", "genshin", "hello"}
element = my_set.pop()
print(element)
# 清空集合， 集合.clear()
my_set.clear()
print(my_set)
# 取出两个集合的差集（集合1有集合2没有的） 集合1.difference(集合2) 返回一个新集合，原来的两个集合不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
# print(set3)
# 消除2个集合的差集 集合1.difference_update(集合2) 在集合1内，删除和集合2相同的元素，集合1被修改，集合2不变
set1.difference_update(set2)
print(set1)
# 合并两个集合 集合1.union(集合2) 得到新集合，原来的两个集合不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set3)
# 统计集合元素数量len()
print(len(set3))
# 集合的遍历 用for循环
for x in set3:
    print(x)


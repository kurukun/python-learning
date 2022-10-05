# 文件操作基本可以分为 打开 关闭 读 写
# 打开文件
f = open("E:/zql-Workstation/test.txt", "r", encoding="UTF-8")
my_str = f.read()
print(my_str.count('1'))
# print(type(f))
# 读操作相关方法
# 读取文件 - read(num) num表示读取多少字节，不填默认读取整个文件
# print(f"读取10个字节的结果：\n{f.read(10)}")
# 连续调用两次read的话会从前一次read的结尾继续
# print(f"读取全部字节的结果：\n{f.read()}")
# 读取文件 - readlines() 读取文件的全部行，封装到列表中, readline() 一次只读取一行内容，返回值类型为字符串
# lists = f.readlines()
# print(type(lists))
# print(lists)

# for循环读取文件行
# for line in f:  # line可以获取每一行的内容
#     print(f"每一行的数据是{line}")

# 文件的关闭 close() 解除python对文件的占用
# f.close()

# with open 语法操作文件
# with open("E:/zql-Workstation/test.txt", "r", encoding="UTF-8") as f:
# 执行完语句块后会自动关闭文件
# for line in f:
#     print(f'每一行的数据是{line}')

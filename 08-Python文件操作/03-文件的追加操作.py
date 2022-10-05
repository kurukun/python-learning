# 与写入操作类似 文件不存在时新建，但文件存在时则把内容写到原有内容之后
f = open('E:/zql-Workstation/world.txt', 'a', encoding='UTF-8')
f.write('这是新增的内容')
f.close()

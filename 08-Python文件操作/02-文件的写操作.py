# open('','w')
# write('xxx') flush()
f = open('E:/zql-Workstation/world.txt', 'w', encoding='UTF-8')  # 如果文件不存在则会新建，若存在则会覆盖文件内原有的内容（全部清空）
f.write('Hello World!')  # 内容写入内存中
f.flush()  # 刷新，将内存中积攒的内容写入到硬盘的文件中，也可以用close方法，它内置了flush功能

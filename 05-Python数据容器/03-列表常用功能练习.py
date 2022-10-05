test_list = [21, 25, 21, 23, 22, 20]
test_list.append(31)
test_list.extend([29, 33, 30])
fir_num = test_list.pop(0)
print(fir_num)
las_num = test_list.pop(len(test_list) - 1)  # 直接用反向索引更好，里面应该写-1
print(las_num)
index = test_list.index(31)
print(index)
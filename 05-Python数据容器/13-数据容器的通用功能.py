# 类型转换
# 容器类型(容器) 将容器转化为容器类型1的容器，是生成新的容器
test_list = [1, 3, 2]
print(type(test_list))
var_box = tuple(test_list)
print(type(var_box))
# 除了无法转字典以外都可以转
# 通用排序功能 sorted(容器, [reverse = False]) reverse参数是可选值，默认为False不反转，并且结果的都是存在列表中
var_box = sorted(test_list, reverse=True)  # 也是不修改原数据
print(var_box)
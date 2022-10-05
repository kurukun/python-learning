# 数据输入 input()
# print("你是谁？")
name = input("你是谁？") # 可以直接在括号内写提示信息
print("我是%s" % name)
# 尝试输入数字类型
num = input("请输入数字")
print("input输入的类型是：%s" % type(num))
# 可见input的默认接收都是字符型，因此想要做数学运算的话还需要进行类型转化
num = int(num)
print("input输入的类型是：%s" % type(num))

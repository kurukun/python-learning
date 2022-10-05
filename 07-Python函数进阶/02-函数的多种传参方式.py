# 位置参数：调用函数时根据函数定义的参数位置来传递参数
# 一直以来使用的大部分函数都是这种方式
def user_info(name, age, gender):
    print(f"您的姓名是{name}，年龄是{age}，性别是{gender}")


user_info('周杰伦', 15, '男')

# 关键字传参：函数调用时通过 键=值 形式传递参数 可以不按顺序写 也可以和位置参数混用，但此时位置参数必须在前面
user_info('蔡依林', age=10, gender='女')


# 缺省参数：用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
# 默认的参数必须写在最后面，否则会报错
def user_info2(name, age, gender='男'):
    print(f"您的姓名是{name}，年龄是{age}，性别是{gender}")


user_info2('小天', 13)
user_info2('小红', 14, '女')


# 不定长参数 又叫可变参数，用于不确定调用的时候会传递多少个参数的场景
# 位置传递 使用关键字*
# 定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info3(*args):
    print(f"args参数的类型是{type(args)}，内容是{args}")


user_info3(1, 2, 3, 'haha', False)


# 关键字传递 使用关键字** 传入形式为键值对
# 定义的形式参数会作为字典存在，接收不定长数量的参数传入
def user_info3(**kwargs):
    print(f"args参数的类型是{type(kwargs)}，内容是{kwargs}")


user_info3(num1=1, num2=2, num3=3, test1='haha', test2=False)

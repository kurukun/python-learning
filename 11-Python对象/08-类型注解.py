from typing import Union
# 对变量的类型进行标记
# 1.为变量设置类型注解
# 注解后有助于IDE进行语法提示，一般无法直接看出变量类型之时会添加变量的类型注解
# 语法：变量:类型
var_1: int = 10
var_2: str = 'hello'
var_3: float = 3.14
var_4: bool = True
# 相当于对变量进行了注释

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"name": 1}
my_str: str = 'hello'
# 容器类型详细注解
my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[int, str, set] = (1, '2', {3})  # 元组的标记需要每一项都标记出来，其他数据容器在混用时则需要Union注解
my_dict2: dict[str, int] = {"name": 1}  # 字典的注解需要两个类型，一个是key一个是value


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 也可以采用注释的方式
var_test = 1  # type: int


# 函数的类型注解，写法与变量的类型注解相似，注解后，调用时ctrl+p便能显示出该填入何种类型的参数，并且使用时也会有相应的提示内容
def add(x: int, y: int):
    print(x + y)


# add()
# 对函数的返回值类型进行注解 使用 ->
def minus(a: int, b: int) -> int:
    return a - b


# Union类型，用于描述有混合类型数据的数据，但使用前必须先导包，函数中也能用
union_list: list[Union[int, str, bool]] = [1, 'haha', True]
union_dict: dict[str, Union[int, str]] = {"name": '周杰棍', "age": 22}

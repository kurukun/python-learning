"""
使用构造方法向成员变量赋值
__init__()
构造类时传入的参数会自动提供给这个方法
构建类的时候该方法会自动执行
"""


class Student:
    def __init__(self, name, age, tel):
        # 上面不定义成员变量的话，则 self.x = y 会在赋值的同时并定义成员变量
        self.name = name
        self.age = age
        self.tel = tel


stu = Student('周杰伦', 22, '1008611')
print(stu.name)
print(stu.age)
print(stu.tel)
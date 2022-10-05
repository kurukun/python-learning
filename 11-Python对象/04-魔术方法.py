# 魔术方法的格式 __方法名__
# __str__()方法
# 控制类转换为字符串的行为 比如print(类名) 一般打印出来的是一个带有内存地址的字符串,但str后可以自定义
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"学生的名字为:{self.name},学生的年龄为:{self.age}"

    # __lt__()方法 __le__()方法与之类似,但变成了<=, __eq__()方法也是,但是变成了 ==,不写eq方法时两个对象之间==也不会报错,但比较是内存地址
    # 小于符号比较方法,用于定义每个对象使用大于小于符号比较时的判断依据
    def __lt__(self, other):
        return self.age < other.age  # 必须是小于,但不知道为什么


stu1 = Student('周杰伦', 18)
stu2 = Student('周杰棍', 22)
print(stu1)  # 没有__str__的话结果为<__main__.Student object at 0x000001BED44BBFD0>

print(stu1 < stu2)
print(stu1 > stu2)

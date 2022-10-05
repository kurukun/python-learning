# 设计类 一般首字母大写
class Student:
    name = None
    gender = None
    age = None
    school = None

    # self是必须有的，但是在使用方法时可以忽略，在定义时若要访问类自身的成员变量必须使用self的点语法
    # 成员行为 一般函数都小写
    def say_age(self):
        print("我今年" + self.age + "岁")


# 创建对象
student = Student()
# 为对象赋值
# 对象属性
student.name = '周杰伦'
student.gender = 'boy'
student.age = '22'
student.school = 'scau'

print(student.name)
print(student.gender)
print(student.age)
print(student.school)
# 对象方法
student.say_age()

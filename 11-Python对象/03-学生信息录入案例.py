class Student:
    name = None
    age = None
    add = None

    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add


students = []
for i in range(10):
    print(f'当前录入第{i + 1}位学生信息，总共需要录入10位学生信息')
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    add = input('请输入学生地址：')
    stu = Student(name, age, add)
    print(f"学生{i}信息录入完成，信息为:【学生姓名：{name}，年龄：{age}，地址：{add}】")
    students.append(stu)

for x in students:
    print(x.name)
    print(x.age)
    print(x.add)

# 函数的作用域以及局部变量和全局变量 基本与以前学的一样
# new 在函数内修改全局变量
num = 200

def test_a():
    print(num)


def test_b():
    # num = 500  # 相当于在函数内又定义了一个局部变量 与外面的num无关系
    global num  # 关键字global声明num是全局变量 则与外面的num是同一个
    num = 500
    print(num)


test_a()
test_b()
print(num)
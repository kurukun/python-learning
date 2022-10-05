# 演示使用多个变量，接收多个返回值
def test_return():
    return 1, 'hello', False

x, y, z = test_return()
print(x)
print(y)
print(z)


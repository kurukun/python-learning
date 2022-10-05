# 无名称的匿名函数，只可以临时使用一次
# 语法：lambda 传入参数: 函数体（只能写一行）
def test_function(x, y, compute):
    result = compute(x, y)
    print(result)


test_function(3, 5, lambda x, y: x + y)  # 临时构建一个函数，只能临时使用一次

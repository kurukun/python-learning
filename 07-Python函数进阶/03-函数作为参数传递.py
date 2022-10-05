def compute(x, y):
    return x + y


# 实际上是逻辑的传递
def test_function(x, y, compute):
    result = compute(x, y)
    print(result)


test_function(3, 5, compute)

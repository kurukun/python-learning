# 函数在不使用return返回数据时的返回值
def say_hi():
    print('hi~')
# 也可以直接在函数内写return None 效果等同于不写return

result = say_hi()
print(result)
print(type(result))

# None用于if判断
def check_age(age):
    if age >= 18:
        return "Success"
    else:
        return None

result = check_age(16)
if not result:
    # 进入if表示result是None值
    print('小朋友，好好学习')

# 用于声明无内容的变量
name = None


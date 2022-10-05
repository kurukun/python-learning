# Python中的if else组合判断
# 格式为在与if同级的位置加一个 else: 如下所示

print("欢迎来到黑马儿童游乐园，儿童免费，成人收费。")
age = input("请输入年龄：")
age = int(age)
if age >= 18:
    print("您已成年，游玩需要补票10元。")
else:
    print("小朋友你好呀！您可以免费游玩")

print("祝您游玩愉快。")

# 判断条件有多个时使用，条件判断的多条件是互斥的，满足一个其他就不执行
# if始 else结
flag = True
while flag:
    age = input("请输入年龄：")
    age = int(age)
    if age >= 30:
        print("恭喜您成为魔法师了。")
    elif age >= 18:
        print("恭喜您成为勇者了。")
    else:
        print("恭喜您成为村民了。")
    select = input("要结束吗？结束则输入y")
    if select == "y":
        flag = False
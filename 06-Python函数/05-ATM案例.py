flag = True
money = 0
while flag:
    print("---------------------主菜单-----------------------")
    print("周杰伦，您好，欢迎来到咕鹭银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款    \t[输入2]")
    print("取款    \t[输入3]")
    print("退出    \t[输入4]")
    num = input("请输入您的选择：")
    num = int(num)
    if num == 1:
        print("---------------------查询余额-----------------------")
        print("周杰伦，您好，您的余额剩余：%d元" % money)
    elif num == 2:
        print("---------------------存款-----------------------")
        temp = int(input("请输入您的存入金额："))
        print(f"周杰伦您好，您存款{temp}元成功")
        money += temp
        print(f"周杰伦您好，您的余额剩余{money}")
    elif num == 3:
        print("---------------------取款-----------------------")
        temp = int(input("请输入您的取款金额："))
        print(f"周杰伦您好，您取款{temp}元成功")
        money -= temp
        print(f"周杰伦您好，您的余额剩余{money}")
    else:
        print("欢迎您下次光临！")
        flag = False

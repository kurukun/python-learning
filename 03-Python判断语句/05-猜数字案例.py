num = int(input())
shot = 1
flag = True
while flag:
    if input("猜猜我心里想的是哪个数字") == num:
        print("恭喜您答对了！")
        flag = False
    elif shot == 1:
        shot += 1
        print("不对，再猜一次")
    elif shot == 2:
        shot += 1
        print("不对，再猜最后一次")
    else:
        print(f"Sorry，全部猜错啦，我想的是：{num}")
        flag = False

import random
workers = range(1, 21)
money = 10000
for i in workers:
    goal = random.randint(1, 10)
    if goal >= 5:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩{money}元")
        if money == 0:
            print("工资发完了，下个月领取吧")
            break
    else:
        print(f"员工{i}，绩效分{goal}，低于5，不发工资，下一位。")
    if i == 20:
        print("全部人的工资安排已完成，下个月见")
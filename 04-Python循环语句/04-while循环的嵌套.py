# 外层循环变量
day = 0
while day < 100:
    print(f"坚持百日冲刺，每天刷10张卷子，今天是第{day + 1}天")
    day += 1
    # 内层的循环变量
    num = 0
    while num < 10:
        print(f"刷第{num + 1}张卷子")
        num += 1

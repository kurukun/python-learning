# continue 跳过本轮循环进入下一轮 又叫临时中断
# break 终止循环 又叫永久中断
# 控制范围只在他们所在的循环中
sum1 = 0
for i in range(6):
    sum1 += i
print(sum1)

sum2 = 0
for i in range(6):
    if i == 2:
        continue  # 下面的语句不会执行
    sum2 += i
print(sum2)

sum3 = 0
for i in range(6):
    if i == 2:
        break
    sum3 += i
print(sum3)

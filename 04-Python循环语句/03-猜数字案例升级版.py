import random
num = random.randint(1, 100)
flag = True
sum = 0
while flag:
    gus_ans = int(input('猜猜我想的是哪一个数字'))
    sum += 1
    if gus_ans == num:
        print('恭喜您答对了，一共猜了%d次' % sum)
        flag = False
    else:
        if gus_ans > num:
            print('大了，再猜一次')
        else:
            print('小了，再猜一次')

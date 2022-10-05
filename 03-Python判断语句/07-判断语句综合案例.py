import random
num = random.randint(1,10)
print(num)
guess_answer = int(input("猜猜我心里想的是哪一个数字？"))

if guess_answer == num:
    print('恭喜您，第一次就答对了')
else:
    if guess_answer > num:
        print('大了，再猜一次')
    else:
        print('小了，再猜一次')
    guess_answer = int(input("猜猜我心里想的是哪一个数字？"))
    if guess_answer == num:
        print('恭喜您，第二次答对了')
    else:
        if guess_answer > num:
            print('大了，再猜最后一次')
        else:
            print('小了，再猜最后一次')
        guess_answer = int(input("猜猜我心里想的是哪一个数字？"))
        if guess_answer == num:
            print('恭喜您，最后一次答对了')
        else:
            print('猜错了，答案是 %d' % num)
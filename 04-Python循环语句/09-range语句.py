# 可以用range语句获取一个数字序列
# range(num) 生成一个从0开始到num结束的数字序列（不包括num本身）
a = range(6)
for x in a:
    print(x, end='')
print()
# range(num1, num2) 生成一个从num1开始到num2结束的数字序列（不包括num本身）
b = range(1,6)
for x in b:
    print(x, end='')
print()
# range(num1, num2, step) 生成一个从num1开始到num2结束的数字序列，但是数字之间的差为2（不包括num本身），若超过上限则不显示
c = range(1, 5, 2)  # 上限为4，所以只能加到3
for x in c:
    print(x, end='')
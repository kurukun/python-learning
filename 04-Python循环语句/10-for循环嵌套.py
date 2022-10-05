# 外层的for循环
for x in range(1, 101):
    print(f"坚持百日冲刺，每天刷10张卷子，今天是第{x}天")
    # 内层的for循环
    for y in range(1, 11):
        print(f"刷第{y}张卷子")
print('坚持到底，成功上岸！')
# 嵌套注意空格缩进！！！

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j}\t", end='')
        j += 1
    print()  # 内容为空就只是换行
    i += 1

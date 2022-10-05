# while循环遍历列表
def while_list():
    my_list = ['are', 'u', 'still', 'in', 'pain', '?']
    i = 0
    while i < len(my_list):
        ele = my_list[i]
        print(f'这是列表的元素{ele}')
        i += 1


# while_list()


def for_list():
    my_list = ['are', 'u', 'still', 'in', 'pain', '?']
    for ele in my_list:
        print(f'这是列表的元素{ele}')


for_list()

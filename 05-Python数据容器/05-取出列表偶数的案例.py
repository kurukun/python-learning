def list_while():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mean_list = []
    i = 0
    while i < len(num_list):
        if num_list[i] % 2 == 0:
            mean_list.append(num_list[i])
        i += 1
    print(f"通过while循环，从列表{num_list}中取出偶数，组成的新列表为：{mean_list}")


def list_for():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mean_list = []
    for ele in num_list:
        if ele % 2 == 0:
            mean_list.append(ele)
    print(f"通过for循环，从列表{num_list}中取出偶数，组成的新列表为：{mean_list}")
list_for()
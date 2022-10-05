my_dict = {
    '王力宏': {
        '部门': '科技部',
        '工资': 3000,
        '级别': 1
    },
    '周杰伦': {
        '部门': '市场部',
        '工资': 5000,
        '级别': 2
    },
    '林俊杰': {
        '部门': '市场部',
        '工资': 7000,
        '级别': 3
    },
    '张学友': {
        '部门': '科技部',
        '工资': 4000,
        '级别': 1
    },
    '刘德华': {
        '部门': '市场部',
        '工资': 6000,
        '级别': 2
    }
}
print(f"全体员工当前信息如下:")
for key in my_dict:
    print(key, my_dict[key])

for key in my_dict:
    if my_dict[key]['级别'] == 1:
        my_dict[key]['级别'] += 1
        my_dict[key]['工资'] += 1000

print(f"升级加薪操作完成后:")
for key in my_dict:
    print(key, my_dict[key])
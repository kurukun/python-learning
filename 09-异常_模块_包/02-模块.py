# 模块的导入
import time
# 使用import导入time模块使用sleep功能
# 这种写法直接把整个模块都导入了
# import time  # 导入python内置的time模块（time.py这个文件）
# print('hello~')
# time.sleep(10)  # 程序执行到这里时会暂停执行10s，通过点就可以使用模块内容的全部功能（类、函数、变量等）
# print('hi~')

# from 模块名 import 功能名(若写*号则导入所有功能)
# 从某一模块导入其中的特定功能,这种写法可以直接写功能名而不用点语法
from time import sleep
print('hello~~')
sleep(3)
print('hi~~~~')

# import 模块名 as 别名 导入模块,并为导入的模块起一个别名,在使用时可以直接用别名替代
# from 模块名 import 功能名 as 别名 导入特定功能,并为它起一个别名,在使用时可以直接用别名替代


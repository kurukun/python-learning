# 包在物理上是一个文件夹,内部包含有许多模块
# 创建一个包
# 导入自定义模块中的包并使用
# 可以通过点语法来控制层级
import my_package.my_module1 as m1
from my_package import my_module2 as m2
# 导入的是什么就可以直接写他的名字来使用,但如果导入的是他的父级,则需要通过点语法把他点出来
m1.add(1, 2)
m2.show_info()

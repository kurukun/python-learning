# 新建一个python文件,在内部定义好函数,然后导入到其他的python文件即可
# 文件名必须要符合标识符命名规则
# 下面这个all变量定义了 from x import * 时能导入的功能,若不定义all则全部功能都可以使用
# 为一个列表
__all__ = ['add']


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


# 整个python文件会内置一个 __name__ 的变量,当在原本文件运行时他的值就会变为'__main__',下面的句子就会变为true,
# 但外部文件引入时则不会,所以不会执行
# 直接main就可以写出来
if __name__ == '__main__':
    print(add(1, 2))


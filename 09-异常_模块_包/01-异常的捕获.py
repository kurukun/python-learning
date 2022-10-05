"""
预测可能会出现bug的代码，当真出现bug时能有后续应对，不至于当出现bug时整个程序停止运行
语法：try:
         可能发生错误的代码
    except:
        如果出现异常执行的代码
"""

# 基本捕获语法 也可以捕获全部异常
# try:
#     f = open('D:/abc.txt', 'r', encoding='UTF-8')
# except:
#     f = open('D:/abc.txt', 'w', encoding='UTF-8')

"""
异常是多种多样的，因此可以捕获指定的异常
格式：
try:
    可能出错的代码
expect NameError(异常类型) as e:
    执行的代码
"""
# 捕获特定的异常
# try:
#     print(name)
# except NameError as e:
#     print('出现了变量未定义的异常')
#     print(e)

# 捕获多个异常 异常类型使用元组
# try:
#     1 / 0
# except (NameError, ZeroDivisionError):
#     print('出现了变量未定义或者除0异常')

# 捕获全部异常
try:
    f = open('D:/abc.txt', 'r', encoding='UTF-8')
    print('hello')
    # 1 / 0
    # print(name)
except Exception as e:
    print('出现异常了')
else:
    print("代码顺利执行完毕，没有出现异常")  # try内的代码执行后没有出现异常会执行的句子，是一个可选的语句
finally:  # 无论有没有异常都要执行的代码，比如打开文件后必须关闭文件，这也是一个可选的句子
    f.close()

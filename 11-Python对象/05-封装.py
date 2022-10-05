"""
演示面向对象封装思想中私有成员的使用
私有成员：对用户隐藏的属性和行为
定义方式：在为私有成员命名时在最前面加上两个下划线
"""
class Say_Hi:
    def hi(self):
        print('sayHi')


class Phone:

    __current_voltage = 0

    def __keep_cpu_single(self):
        print("让cpu以单核模式运行")
        Say_Hi.hi()

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话启动")
        else:
            print("电量不足，无法启动5g通话")
            self.__keep_cpu_single()


phone = Phone()
# 无法被类对象使用，比如上面的phone，但是可以被其他的成员使用(仅在内部使用)，比如上文
# print(phone.__current_voltage)
# phone.__keep_cpu_single()
phone.call_by_5g()

# 复写父类属性：继承了父类的属性，但是又对继承的内容进行修改
class Phone:
    producer = 'HM'

    def call_by_5g(self):
        print('5g通话已开启')

class NewPhone:
    producer = 'KURU'

    def call_by_5g(self):
        # 复写后调用父类成员的方法
        # 方式1
        print(f"父类的厂商是{Phone.producer}")
        Phone.call_by_5g(self)  # 不要漏掉self
        print('5g加强版')
        #  方式2 把上述的父类名写成 super()，此种方法在调用父级的方法时不用传self


# 显示的内容将会是复写后的新内容
phone = NewPhone()
print(phone.producer)
phone.call_by_5g()
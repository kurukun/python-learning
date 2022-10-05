# 语法：class 类名（父类名）: 内容
# 演示单继承
class Phone:
    IMEI = None
    producer = 'HM'

    def call_by_4g(self):
        print('4g通话已开启')


class Phone2022(Phone):  # 括号内为父类名，表示继承父级的其他属性
    # 若要继承多个，则用逗号隔开，如果只是单纯继承而不用增加新功能，则可以使用pass关键字
    # 若继承的属性中有同名属性，则优先级为从左到右，先到先得
    face_id = '10086'

    def call_by_5g(self):
        print('5g通话已开启')


phone = Phone2022()
print(phone.producer)
print(phone.face_id)
# 使用type()方法可以查看字面量或者数据的数据类型
# 字面量
print(type(666))
print(type(3.14))
print(type("hello"))
# 变量
num = 666
flt = 3.14
stg = "nihao"
print(type(num))
print(type(flt))
print(type(stg))
# 使用变量存储type的返回值
str_type = type(666)
print(str_type)

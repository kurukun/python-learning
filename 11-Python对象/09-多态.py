# 同样的行为，传入不同的参数，得到不同的状态
class Animal:
    def speak(self):
        # 具体的实现方法由子类决定，类似这种写法的类被称为抽象类（含有抽象方法）
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪')


class Cat(Animal):
    def speak(self):
        print('喵喵喵')


# 演示多态
def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
# 同样的行为，不同的对象
make_noise(dog)
make_noise(cat)

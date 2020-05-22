# 继承：子类 自动拥有父类中除了私有内容外的所有内容
# 继承的目的：对父类进行扩展


# class Foo:
#     def get_money(self):
#         print("拿钱")
#
# class Bar(Foo):
#     pass
#
# b = Bar()
# b.get_money() # 拿钱 此时调用的是父类中的方法

# 当出现xxx是一种yyy类型的东西，可以使用继承关系
# 猫是一种动物，，猫就可以继承动物
# class Animal:
#     def dong(self):
#         print("动物会动")
#
# class Cat(Animal): # 子类其实是对父类的一种扩展，父类的对象不能执行子类中的功能
#     def nao(self):
#         print("猫会挠人")
#
# c = Cat()
# c.dong() # 动物会动
# c.nao() # 猫会挠人


# class Animal:
#     def dong(self):
#         print("动物会动")
#
# class Cat(Animal): # 子类其实是对父类的一种扩展，父类的对象不能执行子类中的功能
#     def nao(self):
#         print("猫会挠人")
#
#     def dong(self): # 子类中写了与父类一模一样的方法，叫做方法的覆盖，也叫方法的重写
#         print("上蹿下跳")
# 子类其实就是对某一类对象的具体化，具有父类特性，但仍然会有属于该具体事物的特征。
# c = Cat() # 创建的是猫，
# c.dong() # 类中的查询顺序，先找自己，然后再找父类


# python支持多继承
class Foo1:

    def get_money(self):
        print("拿钱")


class Foo2:
    def play(self):
        print("来玩")
    def get_money(self):
        print("给多点")


class Bar(Foo1,Foo2): # 离当前类最近的是亲爹，后面的是干爹
    pass

b = Bar() # 就近原则
b.get_money() # 拿钱，该方法，先到Foo1里面找，再到其他的类里面找
b.play() # 来玩
# # 项目经理
class Base:
#     # 对子类进行约束，必须重写该方法
#     # 在工作以后，拿到公司代码，要先观察有没有NotImplentedError 若有，则继承他，直接重写他
    def login(self):
        # 没有被实现而产生的错误，强行规定子类，必须重写该方法
        raise NotImplementedError("你要重写一下login这个方法，否则报错")  # 抛出异常
#
class Member(Base):
    def login(self):
        print("我是普通人登录")


class Bawu(Base):
    def login(self):
        print("我是吧务人员登录")


# class Houtai(Base):
#     def denglu(self):
#         print("后台登录")
# NotImplemenedError: 你要重写一下login这个方法，否则报错

class Houtai(Base):
    def login(self):
        print("我是后台登录")

# 使用多态模型来整合这些对象中所存在的相同的功能
def deng(obj):  # 多态模型
    obj.login()

# 上层程序员规则不统一 则会进行报错
m = Member()
b = Bawu()
h = Houtai()

deng(m)
deng(b)
deng(h)



# 抽象类和抽象方法
# 抽象方法不需要给出具体的方法体，在抽象类方法中只写一个pass就可以了
# 写抽象方法需要导入模块
# 在一个类中如果有一个方法是抽象方法，那么这个类一定是抽象类
# 如果一个类中所有方法都是抽象方法，那么这个类可以叫做接口类
# 抽象类可作为接口类，抽象方法作为具体的接口，即规定需要存在的功能，在子类中要对规定的方法进行实现


# from abc import ABCMeta, abstractmethod
#
# class Animal(metaclass = ABCMeta ):  # 写完这个类就是抽象类
#     @abstractmethod  # 抽象方法
#     def chi(self): pass  # 这里的吃只是一个抽象概念，没办法很完美的描述出来
#
#     def dongwu(self):  # 抽象方法中可以有正常的方法
#         print("抽象类中可以有正常的方法")
#
#
# # class Cat(Animal):  # 此时猫中也有抽象方法，此时的猫是创建不了对象的
# #     pass
#
# # 通过抽象类的形式也对子类进行了约束，
# class Cat(Animal):
#     def chi(self):  # 重写父类中的抽象方法
#         print("猫喜欢吃鱼")
#
#
#
# c = Cat()
# c.chi()  # 猫喜欢吃鱼
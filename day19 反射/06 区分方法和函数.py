# def func():
#     print("我是个函数")
#
#
# class Foo:
#     def eat(self):
#         print("我是方法")
#
#
# func()
# f = Foo()
# f.eat()
# print(func)  # <function func at 0x0000029D9CD2C268>
# print(f.eat)  # <bound method Foo.eat of <__main__.Foo object at 0x000001773378C0B8>>

# 野路子：打印的结果中包含了function即为函数，打印的结果中带有method即为方法


# 我们的类也是对象，这个对象的特点是：它的属性就是类变量，方法就是类方法
class Foo:
    def shili(self):
        print("我是实例方法")

    @classmethod
    def leifangfa(cls):
        print("我是类方法")

    @staticmethod
    def he():
        print("我是静态方法")


f = Foo()
f.shili()

# 实例方法的第二种调用方式（就今天了解即可）
Foo.shili(f)  # 通过名称空间进行调用,该句相当于f.shili(),此方案不符合面向对象的思想

# 实例方法：
#    1、如果使用对象.实例方法  方法
#    2、如果使用类名.实例方法   函数

# print(Foo.leifangfa)  # <bound method Foo.leifangfa of <class '__main__.Foo'>>
# print(f.leifangfa)  # <bound method Foo.leifangfa of <class '__main__.Foo'>>
#
# # 类方法不管如何调用，他都是方法
#
# print(Foo.he)  # <function Foo.he at 0x00000235C6E412F0>
# print(f.he)  # <function Foo.he at 0x00000235C6E412F0>

# 静态方法都是函数

from types import FunctionType, MethodType

print(isinstance(f.shili, FunctionType))  # False
print(isinstance(Foo.shili, MethodType))  # False


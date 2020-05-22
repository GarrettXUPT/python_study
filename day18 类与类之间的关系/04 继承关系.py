# class Base: # 父类 ——> 基类 ——>超类
#     def chi(self):
#         print("我会吃")
#
# # 派生类——>子类
# class Foo(Base): # 这个类继承了Base，Foo实际上是对Base的扩展
#     def he(self):
#         print("我还会喝")


# class Foo:
#     pass
#
# print(hash(Foo)) # -9223371866184272515 可哈希
# print(hash(Foo())) # -9223371880495196286 可哈希
#
# # 我们创建的类和对象默认都是可哈希的
#
# # 去掉可哈希
#
# class Foo1:
#     __hash__ = None # 此时类所创建的对象就是不可哈希的，但类名却是可哈希的
#
# print(hash(Foo1)) # -9223371894238832430
# print(hash(Foo1())) # 所创建的对象是不可哈希的，但是对应的类名是可哈希的


# class Foo:
#     def chi(self,food):
#         print("我爱吃鱼和",food)
#
# class Bar:
#     def chi(self,food):
#         print("我爱吃肉和",food)
#
# dic = {Foo:"鸡蛋",Bar:"香肠"}
#
# for k,v in dic.items():
#     k().chi(v)
#
# # 我爱吃鱼和 鸡蛋
# # 我爱吃肉和 香肠

# 类名 = 变量名



# class Base:
#     def __init__(self,num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#
# class Foo(Base):
#     def func1(self):
#         pass
#
# object = Foo(123)
# object.func1()
#
#
# class Base:
#     def __init__(self,num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#
#
# class Foo(Base):
#     def func1(self):
#         print("Foo,func1",self.num)
#
# object = Foo(123)
# object.func1() # Foo,func1 123


class Base:
    def __init__(self,num):
        self.num = num

    def func1(self):
        print(self.num)
        self.func2()

    def func2(self):
        print("Base.func2")


class Foo(Base):
    def func2(self):
        print("Foo,func2")

object = Foo(123)  # 可在子类中直接调用父类中的属性
object.func1() # 先在子类里面找，执行到func1后，准备调用func2，func2在Foo里面有，所以调用Foo中的func2

# self就是你访问的那个对象，先找自己，然后再找父类
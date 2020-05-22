# class Base1:
#     def chi(self):
#         print("我是可怜的Base1")
#
# class Base2:
#     def chi(self):
#         print("我是可怜的Base2")
#
# class Base3:
#     def chi(self):
#         print("我是可怜的Base3")
#
# class Base4:
#     def chi(self):
#         print("我是可怜的Base4")
#
# class Bar(Base1, Base2, Base3, Base4):
#     def chi(self):
#         print("我是Bar里面的吃1")
#         # super(类名，self) 从某一类开始找下一个MRO
#         super(Bar, self).chi() # 此时调用的super,在Bar中进行调用，super表示找MRO中的下一个
#         # super().chi()  # super(Bar, self).chi()
#         print("我是Bar里面的吃2")
#
# b = Bar()
# b.chi()
# 我是Bar里面的吃1
# 我是可怜的Base1
# 我是Bar里面的吃2




class Base1:
    def chi(self):
        super().chi()
        print("我是可怜的Base1")

class Base2:
    def chi(self):
        super().chi()
        print("我是可怜的Base2")

class Base3:
    def chi(self):
        print("我是可怜的Base3")

class Base4:
    def chi(self):
        print("我是可怜的Base4")

class Bar(Base1, Base2, Base3, Base4):
    def chi(self):
        print("我是Bar里面的吃1")
        # super(类名，self) 从某一类开始找下一个MRO
        super(Bar, self).chi() # 此时调用的super,在Bar中进行调用，super表示找MRO中的下一个
        # super().chi()  # super(Bar, self).chi()
        print("我是Bar里面的吃2")

b = Bar()
b.chi()
# 我是Bar里面的吃1
# 我是可怜的Base3
# 我是可怜的Base2
# 我是可怜的Base1
# 我是Bar里面的吃2

b1 = Base1()  # 该种情况会报错，因为super表示的下一个MRO没有对象
b1.chi()
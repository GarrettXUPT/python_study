# class Car: # 类名首字母大写，严格遵守驼峰准则
#     pass
#
# # 造车
# c = Car() # 类名（） 即为创建对象
# # 出厂之后进行改装
# c.color = "红色"  # 对象.属性   当属性不存在时，添加属性，若属性存在则表示修改属性
# c.pei = "京A 0001"  # 对象.属性
# c.pailiang = "55L"
#
# print(c.color) # 红色
#
# c.color = "绿色" # 当属性存在的时候为修改属性操作
#
# # 对象.属性 为设置属性信息
#
# c2 = Car()
# c2.color = "蓝色"
# c2.pei = "京A 0002"
# c2.peiliang = "1.6T"
#
# print(c2.color) # 蓝色
#
# class Car:
#     # __init__ 方法是一个特殊的方法，初始化方法，也叫构造方法，
#     # 在创建对象的时候会自动的调用__init__方法
#     # self 就是创建出来的对象
#     def __init__(self,color,pei,peiliang): # 初始化函数，初始化方法，在创建对象的时候，默认执行这个函数,该处是对属性的封装
#         # print("我是init")
#         # print("self = ",self)
#         self.color = color
#         self.pei = pei
#         self.peiliang = peiliang
#         # 车要跑的功能 即为添加函数
#         # 在类中写的函数 叫做方法
#         # self 为当前类的对象
#     def pao(self): # self是自动传递的，不用管它，该处是对动作的封装
#         print("%s我的车能跑" % self.color)
#
#     def jump(self):
#         print("you jump I jump")
#
#
#
# c = Car("绿色","京A 0001","1.6T") # 创建Car类型对象 我是init，此时self参数不需要我们管，在创建对象时需要将初始化的参数赋值
# print(c.color,c.pei,c.peiliang) # 绿色
# c.pao() # 我的车能跑
# c.jump() # you jump I jump



class Phone:
    def __init__(self,color,price,dianchi,num):
        self.color = color
        self.price = price
        self.dianchi = dianchi
        self.num = num

    def call(self,man):
        print("使用%s电话call%s" % (self.color,man))

    def play(self):
        print("电话可以打游戏")

iphone = Phone("黑色","3999","3000","13546043646")
print(iphone.price) # 3999
iphone.call("老刘") # 使用黑色电话call老刘
iphone.play() # 电话可以打游戏

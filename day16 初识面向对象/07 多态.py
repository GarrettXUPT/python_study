# 多态性：同一个对象，多种形态。站在不同的角度，看待同一个事物
# python支持的是鸭子模型,传入进来的功能只要可以调用gagajiao即可

# 为了程序的正常运行，本来是需要传递进来鸭子，但只需要传递进来一个会gagajiao的东西就可以了

# def func(yazi):
#     yazi.gagajiao()

# 动物种类

class Animal:
    def chi(self):
        print("会吃")

class Golden_monkey(Animal):
    def chi(self):
        print("用手拿着吃，五花八门")

class Tigger(Animal):
    def chi(self):
        print("老虎吃肉")

class Elephant(Animal):
    def chi(self):
        print("大象吃香蕉")

# 以下代码是饲养员
# def wei_laohu(lh):
#     lh.chi()
#
# def wei_houzi(hz):
#     hz.chi()
#
# def wei_daixang(dx):
#     dx.chi()

# 万能饲养员
# 优点：超强的可扩展性，面向对象的核心就是多态
def wei_dongwu(dongwu): # 传入的动物会吃就行，即使用传入内容为对象，再来调用其功能
    dongwu.chi()  # 只要传入的对象中具有下列执行的功能即可，再别无其他要求

# 创建动物园

t = Tigger()
m = Golden_monkey()
e = Elephant()

wei_dongwu(t) # 老虎吃肉
wei_dongwu(m) # 用手拿着吃，五花八门
wei_dongwu(e) # 大象吃香蕉
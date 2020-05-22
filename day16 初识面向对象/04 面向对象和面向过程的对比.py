
# 大象装冰箱
# 面向过程
# 脚本 代码是最简单的，不需要构思整个程序的概况
print("开门")
print("装大象")
print("关门")

# 函数式编程,比脚本稍微麻烦一点，对功能有了概况，对功能进行了划分
def kai():
    print("开门")
def zhuang():
    print("装大象")
def guan():
    print("关门")

kai()
zhuang()
guan()

# 面向对象编程
# x先写类，再利用类创建对象，最后利用对象进行相关的操作
class Elephant:
    def __init__(self):
        print("创建了一个大象")

    def kai(self):
        print("开门")

    def zhuang(self):
        print("装大象")

    def guan(self):
        print("关门")

dx = Elephant()
dx.kai()
dx.zhuang()
dx.guan()
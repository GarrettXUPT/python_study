class Computer:

    # 实例方法
    def play(self):
        print("电脑可以用来玩")

    # 在定义实例方法时，必须给出一个参数 self
    # 形参的第一个参数，自动的把对象传递进来
    def work(self): # self 为当前类的对象
        print("电脑可以用来工作")

c = Computer()
c.play() # 实例方法
c.work()

# 字符串操作、列表操作、字典操作、元祖操作等 全都是实例方法
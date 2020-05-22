class Person:
    def play(self,tools):  # 类似多态的使用中的鸭子模型，即一种类功能的实现依赖于另一个类
        tools.run()
        print("玩游戏很开心")


class Computer():
    def run(self):
        print("电脑起来了")


class Phone():
    def run(self):
        print("手机跑起来了")


c = Computer()
ph = Phone()

p = Person()
p.play(c)
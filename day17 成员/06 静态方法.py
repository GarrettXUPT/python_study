class Person:
    def __init__(self, name, id, gender, birth):
        self.name = name    # 实例变量，对象里的变量
        self.id = id
        self.gender = gender
        self.birth = birth
    # 实例方法

    def chi(self):
        print("我会吃")

    @staticmethod  # 静态方法特点就是与class外定义函数没什么区别，即大家都可以对其进行访问
    def yue():  # 方法形参部分可以不放置任何参数
        print("注意学习")


p = Person("吴思睿", "123", "女", "0203")  # 将其实例化为对象

# 注意规范，方法之间空一行，类之间空两行，注释时候，后面要空两格，# 号后端空一格
# 静态方法可以使用对象进行访问，也可以使用类名进行访问，但是一般推介使用类名进行访问
p.yue()  # 注意学习

# 使用类名进行访问,推荐使用类名访问
Person.yue()  # 注意学习
print("你么好")

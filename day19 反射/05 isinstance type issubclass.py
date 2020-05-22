class Animal:
    def chi(self):
        print("刚睡醒，吃点东西")


class Cat(Animal):
    def play(self):
        print("猫喜欢玩")


c = Cat()

# print(isinstance(c, Cat))  # True c与Cat属于同一类型
# print(isinstance(c, Animal))  # True c与Animal是同一类型，向上判断

a = Animal()
# print(isinstance(a, Cat))  # False 动物不一定是猫 不能向下判断
#
# print(type(a))  # 返回a的数据类型 <class '__main__.Animal'>动物类型
#
# print(type([]))  # <class 'list'>
# print(type(c))  # <class '__main__.Cat'> 精准的显示对象的数据类型，及对象属于的类型

# issubclass 判断某类是否为某类的子类 issubclass中的两个参数，一定要是类名
# print(issubclass(Cat, Animal))  # True Cat 为 Animal的子类


# 应用
def cul(a, b):  # 此函数表示两个数字间的相加关系
    # 判断传递进来的对象一定要是数字 int float
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
    else:
        print("输入的数据类型有误")


print(cul(a, c))

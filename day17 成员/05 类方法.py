class Person:
    def __init__(self,name,id,gender,birth):
        self.name = name    # 实例变量，对象里的变量
        self.id = id
        self.gender = gender
        self.birth = birth
    # 实例方法
    def chi(self):
        print("我会吃")

    @classmethod # 装饰器，此时该方法就是类方法
    def he(cls): # 此时接受到的cls是类名，会默认把类名传递给类方法
        print(cls)
        print("我会喝")

# # 用对象进行访问
# p = Person("吴思睿","123","女","0203")
# p.he() # <class '__main__.Person'> 在调用类方法的时候，会默认的把类名传递给类方法
#        # 我会喝


# 类方法一般使用类名来访问，而实例方法使用实例化的对象进行访问
Person.he() # 类方法直接使用类名就可以调用，但实例方法就不允许使用类名来调用，实例方法需要先实例化，后对其中方法进行调用
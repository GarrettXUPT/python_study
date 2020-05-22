class Person:
    def __init__(self,name,id,gender,birth):
        self.name = name    # 实例变量，对象里的变量
        self.id = id
        self.gender = gender
        self.birth = birth
    @property # 将一个方法更改为一个属性，每次使用属性的时候，都会自动的执行这个方法
              # 方法的返回值就是属性值
    def age(self): # 但是该种办法模拟出来的属性是不可以赋值的，只能通过该方法进过处理得到结果
        print("我是方法")
        return 2019 - self.birth

# 在正规的信息存储时，不会写年龄 而是使用生日，省去更新资料时的麻烦
# 年龄这一项，本来就应该是算出来的，而不是直接存储的
p = Person("吴思睿","123","女",2000)

# age = 2019 - p.birth
print(p.age) # 19 看起来像一个变量一样使用，但实际上是调用了一个方法

# p.age = 55 # 不可以对其进行赋值，因为age本质是个方法而不是属性
# 该种办法主要适用于对象的属性是可以被计算出来的，但缺点就是不可以像真的属性一样可以直接赋值
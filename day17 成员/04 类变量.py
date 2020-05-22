class Person:
    country = "中国" # 类变量，直接分享给该类中的其他所有成员
    def __init__(self,name,id,gender,birth):
        self.name = name    # 实例变量，对象里的变量
        self.id = id
        self.gender = gender
        self.birth = birth

p1 = Person("吴思睿","123","女","0101")
p2 = Person("太白","456","女","02.03")

# print(p.name) # 实例变量
# print(p.birth)

print(p1.country)  # 中国 类变量可以给对象来使用
print(p2.country)  # 中国

# p1.country = "大清"  # 没有修改类变量，仅仅给该实例化对象进行了修改
# p2.country = "大明"

Person.country = "大秦"  # 此时对类变量进行了修改，类变量最好使用类名来访问，对类变量所做的修改，会直接同步到所有成员
print(p1.country)  # 大秦
print(p2.country)  # 大秦
Person.country = "大会"
print(p1.country)

class Person:
    def __init__(self, name, id, gender, birth):
        self.name = name    # 实例变量，对象里的变量
        self.id = id
        self.gender = gender
        self.birth = birth

p = Person("wusir","123456","男","96.0102")
print(p.name)
p.birth = "00.01.01"  # 即对初始属性的修改

# 实例变量一般是 对象.变量 来使用
# print(p.birth)
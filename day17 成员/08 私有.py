class Person:
    __qie = "潘潘" # 私有类变量

    def __init__(self,name,id,gender,birth,mimi):
        self.name = name    # 实例变量，对象里的变量
        self.id = id
        self.gender = gender
        self.birth = birth
        self.__mimi = mimi # 私有内容 实例变量 该属性只有在该类中可以使用，其他得不可以调用它，
                           # 私有内容仅仅在类内可以使用，一般作为类内的一种方法

    def __yue(self):
        print("yue")  # 私有的实例方法

    @staticmethod
    def __chi():  # 私有的静态方法
        print("今天，你次了吗")

    @classmethod
    def __he(cls):  # 私有类方法
        print("今天，你和了吗？")

    def gaosu (self):
        print("把秘密告诉了太白，第二天，所有人都知道了%s" % self.__mimi)
        print(Person.__qie) # 私有类变量只能在类中进行调用，除非进过某个方法 对私有内容进行暴露


    # 在类中，私有变量可以随便使用，但是，出了这个类中，没有人会知道，除非专门暴露

p = Person("吴思睿","123","女",2000,"你猜")
# print(p.__mimi) # 此时私有属性不可以被调用,在外界不可以被调用
p.gaosu() # 把秘密告诉了太白，第二天，所有人都知道了你猜
          # 潘潘
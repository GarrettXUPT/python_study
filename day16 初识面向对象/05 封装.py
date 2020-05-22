# 封装
#   1、对属性的封装
#   2、对方法的封装（功能）
#   3、模块
#   4、包

class Student:
    def __init__(self,school,name,num):
        self.school = school
        self.name = name
        self.num = num

    def test(self,subject):
        print( "%s考%s" % (self.name,subject))


s = Student("西电","师宇","20152009")
print(s.num,s.school,s.name) # 将多个信息（值）保存到一个对象中，对属性的封装，即对象实例化以后，即为对其进行封装
s.test("信号") # 对功能的封装
# # 一对一的关系
# class Boy:
#     def __init__(self,name,gril_friend = None): # 将girlfriend设定为默认值，有的话，就将实参传入，没有，则不传
#         # 在初始化的时候，可以给这个类的属性设置为另一个类的对象
#         self.gril_friend = gril_friend # 一个男孩有一个女朋友
#         self.name = name
#
#     def chi(self):
#         if self.gril_friend:
#             print(f"和{self.gril_friend.name}一起去吃饭")
#         else:
#             print("自己吃")
#
#     def movie(self):
#         if self.gril_friend:
#             print(f"和{self.gril_friend.name}一起去看电影")
#         else:
#             print("不去了")
#
# class Gril:
#     def __init__(self,name):
#         self.name = name
#
# b = Boy("wusir")
# g = Gril("太白")
#
# b.chi() #自己吃
#
# b.gril_friend = g
# b.chi() # 和太白一起去吃饭


# 一对多的关系
class School:
    def __init__(self,name):
        self.teach_list = [] # 此处放置多个老师，表示一对多的关系
        self.name = name

    def zhao_pin(self,teacher):
        self.teach_list.append(teacher)

    def shang_ke(self):
        for t in self.teach_list:
            t.work()


class Teach:
    def __init__(self,name):
        self.name = name

    def work(self):
        print(f"{self.name}在工作")


s = School("西电")

t1 = Teach("吴大正")
t2 = Teach("郑东")
t3 = Teach("郭瑞")

s.zhao_pin(t1)
s.zhao_pin(t2)
s.zhao_pin(t3)

s.shang_ke()
# 吴大正在工作
# 郑东在工作
# 郭瑞在工作
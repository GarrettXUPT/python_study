
from random import randint


class Stu:
    def __init__(self, name, num, address, crouse = None):
        self.name = name
        self.num = num
        self.address = address
        self.crouse = crouse
        self.crouse_list = []

    def review(self):
        for c in self.crouse_list:
            print(f"{self.name}选了编号{c.num}，课程名称{c.crouse_name},该门课老师为{c.crouse_teacher.teacher_name},"
                  f"联系电话{c.crouse_teacher.teacher_telephone}")

    def add_crouse(self, crouse):
        self.crouse_list.append(crouse)


class Crouse:
    def __init__(self, num, crouse_name, crouse_teacher = None):
        self.num = num
        self.crouse_name = crouse_name
        self.crouse_teacher = crouse_teacher

    def see(self):
        print(f"该门课程的信息为:{self.num, self.crouse_name, self.crouse_teacher.teacher_name}")

    def set_teacher(self, crouse_teacher):
        self.crouse_teacher = crouse_teacher


class Crouse_teacher:
    def __init__(self, teacher_num, teacher_name, teacher_telephone):
        self.teacher_num = teacher_num
        self.teacher_name = teacher_name
        self.teacher_telephone = teacher_telephone


c1 = Crouse(1, "物理")
c2 = Crouse(2, "化学")
c3 = Crouse(3, "生物")

t1 = Crouse_teacher(11, "海城", 110)
t2 = Crouse_teacher(22, "柏森", 120)
t3 = Crouse_teacher(33, "晓丽", 119)

c1.set_teacher(t1)
c2.set_teacher(t2)
c3.set_teacher(t3)

# s1 = Stu("太白", 111, "北京")
# s2 = Stu("包浪", 222, "天津")
# s3 = Stu("武汉", 333, "武汉")

# s1.add_crouse(c1)
# s1.add_crouse(c2)
#
# s2.add_crouse(c1)
# s2.add_crouse(c3)
#
# s3.add_crouse(c2)
# s3.add_crouse(c3)


# s1.review()
# c1.see()
c_lst = [c1, c2, c3]

stu_list = []
for i in range(30):  # 循环30次
    st = Stu(i+1, "学生" + str(i+1), str(i+1)) # 创建30个学生

    # 随机生成三个数字，对应课程索引
    s = set()  # 使用集合可有效防止选课重复问题
    while len(s) < 2:
        s.add(randint(0, 2))
        # 把随机的三个课程索引对应的课程设置给学生
    for n in s:
        # print(n)  # 随机生成的课程索引
        st.add_crouse(c_lst[n])
    # 加到列表
    stu_list.append(st)
# 显示学生的选课情况及对应老师的电话
for s in stu_list:
    print(f"学生编号：{s.num},学生姓名：{s.name}")

    # 拿到学生的课程信息
    for c in s.crouse_list:
        print(f"\t课程编号{c.crouse_name} 课程名称{c.crouse_name} 任课老师{c.crouse_teacher.teacher_name} 老师电话{c.crouse_teacher.teacher_telephone} ")

'''
面向对象：
    1、先写类，明确其属性与功能 即对需求了如指掌
    2、对象就是一坨内存地址
'''
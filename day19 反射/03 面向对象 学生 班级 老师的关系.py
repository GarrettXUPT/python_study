class Stu:
    def __init__(self, name, num, cla = None):
        self.name = name
        self.num = num
        self.cla = cla


class Cla:
    def __init__(self, name):
        self.name = name
        self.teach_list = []
        self.student_list = []


class Tec:
    def __init__(self, name):
        self.name = name
        self.cla_list = []


s1 = Stu("宝宝", 1)
s2 = Stu("你好", 2)
s3 = Stu("干嘛", 3)
s4 = Stu("太白", 4)

c1 = Cla("小班")
c2 = Cla("中班")
c3 = Cla("大班")

t1 = Tec("海城")
t2 = Tec("柏森")
t3 = Tec("晓丽")

s1.cla = c1
s2.cla = c2
s3.cla = c3
s4.cla = c1

c1.teach_list.append(t1)
c1.teach_list.append(t2)

c2.teach_list.append(t2)
c2.teach_list.append(t3)

c3.teach_list.append(t1)
c3.teach_list.append(t3)

t1.cla_list.append(c1)
t1.cla_list.append(c3)

t2.cla_list.append(c1)
t2.cla_list.append(c2)

t3.cla_list.append(c2)
t3.cla_list.append(c3)
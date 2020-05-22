import os

class Student:
    def __init__(self, sname, login_name, login_pwd, lst = None):
        self.login_name = login_name
        self.login_pwd = login_pwd
        self.sname = sname
        self.lst = []

    @staticmethod  # 就是为了方便下系统方便调用，所以使用静态方法
    def stu_display():
        f = open("stu", mode="r", encoding="utf_8")
        i = 1
        for el in f:
            d = eval(el.strip())
            print("%s 学生姓名:%s  学生登录名:%s  学生登录密码:%s " % (i, d["sname"], d["login_name"], d["login_pwd"]))
            i = i + 1
        f.close()

    def xuanke(self):  # self是当前登陆的学生
        # 显示所有课程
        Crouse.all_display()
        num = int(input("请输入你要选择的课程编号"))
        f = open("cro", mode="r", encoding="utf-8")
        for i in range(num):
            line = f.readline()

            if line.strip() in self.lst:
                print("你已经选过该课程")

            else: # 没选过该课程
                self.lst.append(line.strip())
                self.write_to_file()
                print("选课成功")

        f.close()
        y = input("是否继续选课？(Y/N)")
        if y != "Y":
            return

    def write_to_file(self):  # 用来同步文件信息
        with open("stu", mode="r", encoding="utf-8") as f1, \
            open("stu_副本", mode="w", encoding="utf-8") as f2:
            for line in f1:
                d = eval(line.strip())
                if d["login_name"] == self.login_name and d["login_pwd"] == self.login_pwd:
                    f2.write(str(self.__dict__) + "\n")
                else:
                    f2.write(line)
        os.remove("stu")
        os.rename("stu_副本", "stu")

    def loading(self):  # 此处self就是当前正在登陆的学生
        f =  open("stu", mode="r", encoding="utf-8")
        for line in f:
            d = eval(line.strip())
            if d["login_name"] == self.login_name and d["login_pwd"] == self.login_pwd:
                cro_list = d["lst"]  # 拿到学生的课程信息
                self.lst = cro_list  # 将拿到的课程信息，放在学生对象里
                f.close()
                break

    def shanchu(self):
        for i in range(len(self.lst)):
            print(i + 1,self.lst[i])

        num = int(input("请输入你要删除的课程"))
        self.lst.pop(num-1)
        self.write_to_file()
        print("删除成功")


class Crouse:
    def __init__(self, crouse_name, crouse_teach, crouse_teach_tele):
        self.crouse_teach = crouse_teach
        self.crouse_name = crouse_name
        self.crouse_teach_tele = crouse_teach_tele

    @staticmethod
    def all_display():
        with open("cro", mode="r", encoding="utf-8") as f:
            i = 1
            for el in f:
                d = eval(el.strip())
                print("课程编号:%s  课程名称:%s  任课老师:%s  老师联系方式:%s" % (i, d["cro"], d["cro_teach"], d["cro_teach_tele"]))
                i = i + 1


class Client:
    def __init__(self):
        self.stu = None  # 记录登录的学生状态

    def admin_client(self):
        print('''
        欢迎进入管理员系统
        1、创建课程
        2、创建学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生选课情况
        6、返回
        ''')
        while 1:
            num = input("请输入你要进行的操作")
            if num == "1":
                cro = input("请输入你要创建的课程名称")
                cro_teach = input("请输入该课程的任课老师")
                cro_teach_tele = input("请输入任课老师联系电话")
                c = Crouse(cro , cro_teach, cro_teach_tele)
                f = open("cro", mode="a", encoding="utf-8")
                f.write(str(c.__dict__)+ "\n")
                f.flush()
                f.close()
            elif num == "2":
                name = input("请输入学生姓名")
                login_name = input("请输入需要创建的用户名：")
                login_pwd = input("请输入登录密码")
                stu = Student(name,login_name, login_pwd )
                # 将学生对象中的内容写在文件中
                f1 = open("stu", mode = "a", encoding = "utf-8")
                f1.write(str(stu.__dict__) + "\n")
                f1.flush()
                f1.close()
                print("======创建学生成功======")
            elif num == "3":
                Crouse.all_display()
            elif num == "4":
                Student.stu_display()
            elif num == "5":
                with open("stu", mode="r", encoding="utf-8") as f:
                    for el in f:
                        dic = eval(el.strip())
                        print("%s 选了 %s课" % (dic["sname"], dic["lst"]))
            elif num == "6":
                return
            else:
                print("输入错误，请重新输入")

    def stu_client(self):
        print("=======同学，欢迎来到教务======")
        while self.stu == None:
            uname = input("请输入用户名")
            upwd = input("请输入密码")
            with open("stu", mode="r", encoding="utf-8") as f:
                for el in f:
                    dic = eval(el.strip())
                    if uname == dic["login_name"] and upwd == dic["login_pwd"]:
                        print("======登陆成功======")
                        # 本题灵魂,必须记录当前登录学生
                        self.stu = Student(dic["sname"], dic["login_name"], dic["login_pwd"])
                        self.stu.loading()  # 加载出当前学生的课程信息
                        break
                    else:
                        print("登录失败")

            while 1:
                print('''
                请选择系统功能：
                1、查看所有课程
                2、选择课程
                3、查看已选课程
                4、删除已选课程
                5、退出
                ''')
                while 1:
                    num = input("请输入你的操作")
                    if num == "1":
                         Crouse.all_display()
                    elif num == "2":
                        self.stu.xuanke()
                    elif num == "3":
                        for c in self.stu.lst:
                            print("已选课程 %s" % c)
                    elif num == "4":
                        self.stu.shanchu()
                    elif num == "5":
                        return
                    else:
                        print("输入有误，请重新输入")


    def run(self):
        while 1:
            print("=========欢迎进入学生选课系统========")
            num = input("您是学生(1)还是管理员(2),Q:退出系统")
            if num == "1":
                print("=======进入学生界面======")
                self.stu_client()
            elif num == "2":
                print("=======进入管理员界面======")
                self.admin_client()
            elif num.upper() == "Q":
                print("正在退出.........")
                exit()
            else:
                print("输入错误，请重新输入")

c = Client()
c.run()
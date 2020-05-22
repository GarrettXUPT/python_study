class Student:
    def __init__(self, login_name, login_pwd,  lst = None):
        self.login_name = login_name
        self.login_pwd = login_pwd
        # self.sanme = sname
        # self.lst = []

    def choiced_review(self):  # 查看已选课程
        with open(self.login_name+"stu_cro_file", mode="r", encoding="utf-8") as f:
            for el in f:
                d = eval(el.strip())
                print("已选课程为 %s 任课老师 %s" % (d["crouse_name"], d["crouse_teacher"]))

    def all_review(self):  # 查看所有课程
        with open("cro_file", mode="r", encoding="utf-8") as f:
            for el in f:
                d = eval(el.strip())
                print("课程名称 %s 任课老师 %s" % (d["crouse_name"], d["crouse_teacher"]))

    def choice(self):  # 选择课程
        with open("cro_file", mode = "r", encoding = "utf-8") as f2:
            for el in f2:
                d = eval(el.strip())
                print("课程名称 %s  任课老师 %s" % (d["crouse_name"],d["crouse_teacher"]))
            with open("cro_file", mode="r", encoding="utf-8") as f2:
                f =  open(self.login_name+"stu_cro_file", mode="a", encoding="utf-8")
                name = input("请输入所选课程名称")
                for el in f2:
                    d = eval(el.strip())
                    if name == d["crouse_name"]:
                        f.write(str(d)+"\n")

                        print("===选课成功===")
                        f.flush()
                        f.close()


class Manager:
    def add_crouse(self):
        print("====进入新增课程界面====")
        crouse_name = input("请输入要新增的科目名称")
        crouse_teacher = input("请输入该科目的任课老师")
        cro_dic = {"crouse_name":crouse_name, "crouse_teacher":crouse_teacher}
        with open("cro_file", mode = "a", encoding = "utf-8") as f:
            f.write(str(cro_dic) + "\n")
            f.flush()
            f.close()
        print("======创建课程成功======")

    def add_stu(self):
        print("======进入新增学生界面=======")
        login_name = input("请输入需要创建的用户名：")
        with open("stu_file", mode = "r", encoding = "utf-8") as f:
            for stu in f:
                # 将字符串转化为字典
                dd = eval(stu.strip())
                if dd["login_name"] == login_name:
                    print("该用户已存在，请重新创建")
                    f.close()
            else:
                print("该用户名可用")
        login_pwd = input("请输入创建账号的密码：")

        stu_dic = {"login_name":login_name, "login_pwd":login_pwd}
        with open("stu_file", mode = "a", encoding = "utf-8") as f:
            f.write(str(stu_dic) + "\n")
            f.flush()
            f.close()
        s = Student(login_name, login_pwd)
        print("创建成功")

    def all_stu(self):
        with open("stu_file", mode = "r", encoding = "utf-8") as f:
            for el in f:
                dd = eval(el.strip())
                print("用户名%s,登录密码%s" % (dd["login_name"], dd["login_pwd"]))

    def stu_choice(self):

        with open("cro_file", mode="r", encoding="utf-8") as f:
            for el in f:
                dd = eval(el.strip())
                print("用户名%s 选课%s" % (dd["crouse_name"], dd["crouse_teacher"]))
    #
    def all_crouse(self):
        with open("cro_file", mode="r", encoding="utf-8") as f:
            for el in f:
                d = eval(el.strip())
                print("课程名称 %s 任课老师 %s" % (d["crouse_name"],d["crouse_teacher"]))

def stu_login():
    def stu_system(s):
        print("=======同学，欢迎来到教务======")
        print('''
        请选择系统功能：
        1、查看所有课程
        2、选择课程
        3、查看已选课程
        4、删除已选课程
        5、退出
        ''')
        ff = True

        while ff:
            num = input("请输入你的操作")
            if num == "1":
                s.all_review()
            elif num == "2":
                s.choice()
            elif num == "3":
                s.choiced_review()
            elif num == "4":
                s.del_choice()
            elif num == "5":
                ff = False
            else:
                print("输入有误，请重新输入")
    a =1
    while a < 2:
        username = input("请输入用户名")
        userpwd = input("请输入密码")
        with open("stu_file", mode="r", encoding="utf-8") as f1:
            for el in f1:
                d = eval(el.strip())
                if username == d["login_name"] and userpwd == d["login_pwd"]:
                    s = Student(username, userpwd)
                    stu_system(s)
                    a = a + 1
            else:
                print("登录失败，请重新登录")

def man_system(manager):
    name = "Garrett"
    pwd = "1234"
    while 1:
        n = input("请输入管理员用户名")
        p = input("请输入管理员密码")
        if n == name and p == pwd:
            print('''
            欢迎进入管理员系统
            1、创建课程
            2、创建学生账号
            3、查看所有课程
            4、查看所有学生
            5、查看所有学生选课情况
            6、退出
            ''')
            while 1:
                num = input("请输入你要进行的操作")
                if num == "1":
                    manager.add_crouse()
                elif num == "2":
                    manager.add_stu()
                elif num == "3":
                    manager.all_crouse()
                elif num == "4":
                    manager.all_stu()
                elif num == "5":
                    manager.stu_choice()
                elif num == "6":
                    return
                else:
                    print("输入错误，请重新输入")
            else:
                print("登录失败，请重新输入")


print("===欢迎来到课程管理系统===")
e = input("您是学生(1) 管理员(2)")
if e == "1":
    stu_login()
elif e == "2":
    m = Manager()
    man_system(m)





# class Student:
#     def __init__(self, login_name, login_pwd, sname, lst = None):
#         self.login_name = login_name
#         self.login_pwd = login_pwd
#         self.sanme = sname
#         self.lst = []
#
#
# class Crouse:
#     def __init__(self, crouse_name):
#         self.crouse_name = crouse_name
#
#
# class Client:
#     def admin_client(self):
#         print('''
#         欢迎进入管理员系统
#         1、创建课程
#         2、创建学生账号
#         3、查看所有课程
#         4、查看所有学生
#         5、查看所有学生选课情况
#         6、返回
#         ''')
#         while 1:
#             num = input("请输入你要进行的操作")
#             if num == "1":
#                 manager.add_crouse()
#             elif num == "2":
#                 def add_stu(self):
#                     name = input("请输入学生姓名")
#                     login_name = input("请输入需要创建的用户名：")
#                     with open("stu_file", mode = "r", encoding = "utf-8") as f:
#                         for stu in f:
#                             # 将字符串转化为字典
#                             dd = eval(stu.strip())
#                             if dd["login_name"] == login_name:
#                                 print("该用户已存在，请重新创建")
#                                 f.close()
#                         else:
#                             print("该用户名可用")
#                     login_pwd = input("请输入创建账号的密码：")
#
#                     stu_dic = {"login_name":login_name, "login_pwd":login_pwd}
#                     with open("stu_file", mode = "a", encoding = "utf-8") as f:
#                         f.write(str(stu_dic) + "\n")
#                         f.flush()
#                         f.close()
#                     s = Student(login_name, login_pwd, name)
#
#             elif num == "3":
#                 manager.all_crouse()
#             elif num == "4":
#                 manager.all_stu()
#             elif num == "5":
#                 manager.stu_choice()
#             elif num == "6":
#                 return
#             else:
#                 print("输入错误，请重新输入")
#
#
#
#     def stu_client(self):
#         print("=======同学，欢迎来到教务======")
#         print('''
#         请选择系统功能：
#         1、查看所有课程
#         2、选择课程
#         3、查看已选课程
#         4、删除已选课程
#         5、退出
#         ''')
#         while 1:
#             num = input("请输入你的操作")
#             if num == "1":
#                 student.all_review()
#             elif num == "2":
#                 student.choice()
#             elif num == "3":
#                 student.choiced_review()
#             elif num == "4":
#                 student.del_choice()
#             elif num == "5":
#                 return
#             else:
#                 print("输入有误，请重新输入")
#
#
#     def run(self):
#         while 1:
#             print("=========欢迎进入学生选课系统========")
#             num = input("您是学生(1)还是管理员(2)")
#             if num == "1":
#                 print("=======进入学生界面======")
#                 self.stu_client()
#             elif num == "2":
#                 print("=======进入管理员界面======")
#                 self.admin_client()
#             else:
#                 print("输入错误，请重新输入")
#
# c = Client()
# c.run()
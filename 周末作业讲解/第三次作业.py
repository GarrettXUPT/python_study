# 模仿博客园系统
login_name = ""
flag = False

def login_verify(fn):
    def inner(*args, **kwargs):
        while 1:
            if flag == True:
                ret = fn(*args, **kwargs)
                return ret
            else:
                print("您还没有登录，请登录")
                login()
    return inner




def login():
    print("======欢迎进入登录环节======")
    ff = True
    while ff:
        uname = input("请输入用户名")
        upwd = input("请输入密码")
        f = open("register" ,mode = "r", encoding = "utf-8")
        for line in f:
            # 将字符串变为字典
            d = eval(line.strip())
            if uname == d["username"] and upwd == d["password"]:
                print("======登陆成功======")
                global login_name, flag
                login_name = uname  # 保存登陆的用户名
                flag = True     # 改变登录状态
                f.close()
                ff = False
                return  # 回到系统主界面
        f.close()
        r = input("======登录失败 是否重新登录(Y/N)======")
        if r.upper() == "N":  # 忽略大小写操作
            ff = False

def regist():
    print("=======进入注册环节！=======")
    ff = True
    while ff:
        uname = input("请输入你的用户名：")
        # 判断用户名是否重复
        f = open("register", mode = "r", encoding = "utf-8")
        for line in f:  # 将该循环迭代完成后，开始执行else
            # 字符串转化为字典
            dd = eval(line.strip())
            if uname == dd["username"]:
                print("用户名重复，请重新输入")
                f.flush()
                f.close()
                break  # 打断的是当前for循环
        else:  # 用户名不重复，可用
            print("用户名可用")
            ff = False
            f.flush()
            f.close()
    uwpd = input("请输入你的密码：")

    d = {"username":uname,"password":uwpd}
    f = open("register", mode = "a", encoding = "utf-8")
    f.write(str(d) + "\n")
    f.flush()
    f.close()
    # 创造用来存放文章和日记的文件
    f1 = open("article_" + uname, mode = "w", encoding = "utf-8")
    f2 = open("diary_" + uname, mode = "w", encoding = "utf-8")
    f1.close()
    f2.close()
    print("=======注册成功！=======")


def read_article():
    print("======读文章环节=======")
    with open("article" + login_name, mode = "r", encoding = "utf-8") as f:
        count = 1
        for line in f:
            id = eval(line.strip())
            print(count,id["title"])
            count = count + 1
    while 1:
        a = input("请输入你要读的文章, Q 返回上一单元")
        if a.upper() == "Q":
            return
        else:
            id = int(a)
        if id < 1 or id > count:
            print("该文章不存在,请重新输入")
            continue
        else:
            with open("article" + login_name, mode="r", encoding="utf-8") as f:
                for i in range(id):
                    line = f.readline()

            # 此时读取的line就是第id行的数据
            dd = eval(line.strip())
            print("您选择的文章标题是:%s" % dd["title"])
            print("您选择的文章内容为:")
            print(dd["content"])

def read_diary():
    print("======读日记环节=======")
    with open("diary" + login_name, mode = "r", encoding = "utf-8") as f:
        count = 1
        for line in f:
            id = eval(line.strip())
            print(count,id["title"])
            count = count + 1
    while 1:
        a = input("请输入你要读的日记, Q 返回上一单元")
        if a.upper() == "Q":
            return
        else:
            id = int(a)
        if id < 1 or id > count:
            print("该日记不存在,请重新输入")
            continue
        else:
            with open("diary" + login_name, mode="r", encoding="utf-8") as f:
                for i in range(id):
                    line = f.readline()

            # 此时读取的line就是第id行的数据
            dd = eval(line.strip())
            print("您选择的日记标题是:%s" % dd["title"])
            print("您选择的日记内容为:")
            print(dd["content"])


def write_article():
    title = input("请输入你要写的文章标题")
    content = input("请输入你写的文章内容")
    d = {"title":title, "content":content}
    with open("diary" + login_name , mode = "a", encoding = "utf-8" ) as f:
        f.write(str(d) + "\n")
    print("=======写入文章成功=======")

def write_diary():
    title = input("请输入你要写的日记标题")
    content = input("请输入你写的日记内容")
    d = {"title":title, "content":content}
    with open("diary" + login_name , mode = "a", encoding = "utf-8" ) as f:
        f.write(str(d) + "\n")
    print("=======写入日记成功=======")


@login_verify
def article():
    while 1:
        print("=======欢迎来到文章环节======")
        while 1:
            print("1、读文章")
            print("2、写文章")
            print("3、返回")
            num = input("你要执行的操作")
            if num == "1":
                read_article()
            elif num == "2":
                write_article()
            elif num == "3":
                print("======结束文章环节======")
                return   # 回到系统主界面
            else:
                print("输入无效指令")

@login_verify
def diary():
    while 1:
        print("=======欢迎来到日记环节======")
        while 1:
            print("1、读日记")
            print("2、写日记")
            print("3、返回")
            num = input("你要执行的操作")
            if num == "1":
                read_diary()
            elif num == "2":
                write_diary()
            elif num == "3":
                print("======结束日记环节======")
                return  # 回到系统主界面
            else:
                print("输入无效指令")






print("欢迎来到博客园系统")
mean = ("登录", "注册", "文章", "日记", "退出")

while 1:
    for i in range(len(mean)):
        print(i+1 , mean[i])

    m = input("请输入你要执行的操作")

    if m == "1":
        login()
    elif m == "2":
        regist()
    elif m == "3":
        article()
    elif m == "4":
        diary()
    elif m == "5":
        exit()
    else:
        print("你输入的操作有误！")



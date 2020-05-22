menu = ("查看","修改","添加","删除","退出")

flag = False # 没登录
def login():
    global flag
    usename = input("请输入用户名")
    password = input("请输入密码")
    if usename == "alex" and password == "123":
        print("登陆成功")
        flag = True
    else:
        print("用户名 密码错误")
        flag = False


# 登录验证装饰器
def login_verify(fn):
    def inner(*args,**kwargs):
        # 登陆的校验
        while 1:
            if flag == True:
                ret = fn(*args,**kwargs)
                return ret
            else:
                print("对不起，您还没有登录，请登录")
                login()
    return inner


@login_verify
def chakan():
    print("查看")
@login_verify
def xiugai():
    print("修改")
@login_verify
def tianjia():
    print("添加")
@login_verify
def shanchu():
    print("删除")

while 1:
    for i in range(len(menu)):
        print(i + 1,menu[i])

    num = input("请输入你要的操作")
    if num ==  "1":
        chakan() # 查看
    elif num == "2":
        xiugai() # 修改
    elif num == "3":
        tianjia() # 添加
    elif num == "4":
        shanchu() # 删除
    elif num == "5":
        pass # 退出
        print("程序退出中........")
        exit()
    else:
        print("输入信息有误，请重新选择")
 # class Person: # 确定创建的类型
#     def __init__(self,waihao,name,address): # 该类型的事物都有哪些共同特征
#         self.waihao = waihao
#         self.name = name
#         self.address = address
#         self.iq = 250
#     def tigger(self):
#         print("打老虎")
#     def shaozi(self):
#         print("%s可以杀嫂子" % self.name)
#     def titianxingdao(self):
#         print("%s可以替天行道" % self.name)
#
# wusong = Person("行者","武松","高老庄")
# wusong.tigger()
# wusong.shaozi()
# wusong.titianxingdao()
# print(wusong.name,wusong.waihao,wusong.address,wusong.iq)

# 用户登录的问题，逻辑是活的

# 我的版本：将所有逻辑写在类中
Flag = False
class User:


    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        usname = input("请输入你的用户名")
        paswod = input("请输入你的密码")

        if usname == self.username and paswod == self.password:
            print("登陆成功")
            Flag = True

        else:
            print("登录失败")

    def verify_login(self, fn):
        def inner(*args, **kwargs):
            while 1:
                if Flag == True:
                    ret = fn(*args, **kwargs)
                    return ret
                else:
                    self.login()
        return inner

u = User("alex","123")
u.login()
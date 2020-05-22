# MD5 用来加密，并且是不可逆算法，但是可以通过撞库进行破解
import hashlib

# # 创造一个MD5对象
# obj = hashlib.md5(b"dyudgyuagdygdtyefydeuagdytfwydfwydauyugdyudtyf")  # 加盐，在程序中，盐是固定的
# obj.update("123456".encode("utf-8"))  # 将要加密的内容，传递给MD5
# print(obj.hexdigest())  # 拿到秘文
# # 加盐前（可通过撞库进行破解）：534b44a19bf18d20b71ecc4eb77c572f
# # 加盐后（不可破解）：bc55dad932039f04408cc8ecd64c76c3

# MD5主要用途
# MD5定义函数

obj = hashlib.md5()  # 加盐，随即对其添加比特串
obj.update(s.encode("utf-8"))  # 将要加密的内容，传递给MD5
print(obj.hexdigest())  # 拿到秘文
# 数据库里：
username = "Garrett"
password = "5d0e32e908a88dc28bc296548bd90d6b"

# MD5加盐原理：每次保存密码到数据库时，都生成一个随机比特串，将这些比特串和密码相加再求MD5摘要，
# 然后在摘要中再将这些比特串按规则掺入形成一个48位的字符串。在验证密码时再从48位字符串中按规则这些比特串，
# 和用户输入的密码相加再MD5。按照这种方法形成的结果肯定是不可直接反查的，且同一个密码每次保存时形成的摘要也都是不同的。

# 登录
uname = input("请输入你的用户名")
upwd = input("请输入你的密码：")

if uname == username and my_md5(upwd) == password:
    print("登录成功")
else:
    print("登录失败")
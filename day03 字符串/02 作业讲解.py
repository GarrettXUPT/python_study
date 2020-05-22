
# from random import randint # 导入工具包
#
# left = 1
# right = 100
# n=randint(1,100) #生成1-100的随机数
# count = 1
# while count <= 3 :
#     num = int(input("请输入随机的一个数（%s-%s）：" % (left,right)))
#     if num > n:
#         print("猜大了")
#         right = num # 范围缩小
#     elif num < n:
#         print("猜小了")
#         left = num  # 范围缩小
#     else:
#         print("猜对了")
#         break
#     count = count + 1
# print("你太笨了")

# 正确的用户名和密码
# name = "周杰伦"
# password = "123"
#
# count = 3
# while count >= 1:
#     print("还剩下%s次机会" % count)
#     name1 = input("请输入你的用户名：")
#     password1 = input("请输入你的密码：")
#     if name1 == name and password1 == password:
#         print("欢迎进入系统")
#         break
#     else:
#         print("用户名或者密码错误")
#     count = count - 1
# if count == 0:
#     print("你的账号已被封锁")

# 判断一个数为几位数

num = 9800
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print(count)
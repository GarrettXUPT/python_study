# # 生成随机四位验证码
# from random import randint
#
# goods = [{"name":"电脑","price":1999},
#          {"name":"鼠标","price":19},
#          {"name":"游艇","price":999},
#          {"name":"美女","price":199}
#         ]
# # 用户登录信息
# name = "shiyu"
# passcode = "123456"
# # 准备一个购物车 购物车[{"id":"编号","name":"名称","price":"价格","totle":"商品数量"}]
# shopping = []
#
# num = 0
# verify_code = ""
# while num < 4:
#     verify_code = verify_code + chr(randint(65,90))  # (65,90)对应英文字母的分布（A，Z）
#     num = num + 1
# count = 0
# while count < 3:
#     user = input(f"请输入用户名：（你还剩下{3-count}次机会）").strip()
#     passcode_user = input("请输入密码：").strip()
#
#     if user == name and passcode_user == passcode:
#         print(verify_code)
#         vc = input("请输入验证码：").strip().upper()
#         if  vc == verify_code:
#             print("欢迎进入系统")
#
#             money = int(input("请输入你的工资"))
#             while 1:
#                 for i in range(len(goods)):
#                     print(i + 1,goods[i]['name'],goods[i]['price'])
#                     # 1 电脑 1999
#                     # 2 鼠标 19
#                     # 3 游艇 999
#                     # 4 美女199
#                 num = int(input("请输入你要购买的商品编号"))  # 还没判断是否是数字
#                 # 还原回索引
#                 index = num -1
#                 # 获取到购买的商品
#                 good = goods[index]
#                 # 判断是否可以购买该商品
#                 if money > good['price']:
#                     # print("可以购买")，并判断是否已经购买过商品，若买过，则只需要将其数量加一，若没买过，则将其加到购物车里即可
#                     for el in shopping: # el 表示你已经购买过的商品
#                         if el['id'] == index: # 你已经购买的商品
#                             el['totle'] = el['totle'] + 1
#
#                             break # 继续显示商品列表
#                     else: # 表示该商品没买过
#                         shopping.append({"id":index,"name":good['name'],"price":good['price'],"totle":1})
#                     money = money - good['price']
#                     print(f"购买成功，你的余额是{money}")
#                     iscontinue = input("请问是否继续购物：(Y/N)")
#                     if iscontinue.upper() == "N":
#                         for g in shopping:
#                             print(g['name'],g['price'],g['totle'])
#                         print(f"你的余额{money}")
#                         exit()  # 程序退出
#                     else:
#                         continue
#
#
#                 else:
#                     print(f"余额不足！还剩{money}")
#
#         else:
#             print("验证码错误")
#     else:
#         print("用户名或密码错误，请重新输入")
#     count = count + 1
# print("登录失败")

# # 判断输入的几位数
# num = int(input("请输入你的数字："))
# count = 0
# while num > 0:
#     num = num //10
#     count = count + 1
# print(count)

# # 求多少位的小数
# num = input("请输入你的小数：")
# c = len(num[num.index(".")+1:])
# print(c)


# 素数，只能被1或自身整除的数
for n in range(2,10000):
#n = int(input("请输入一个数字："))
    for i in range(2,n):  # i从2 到n-1
        if n % i == 0:
            #print("该数字不是素数")
            break
    else:
        # print("该数字为素数")
        print(n)



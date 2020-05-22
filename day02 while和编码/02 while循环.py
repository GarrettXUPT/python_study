
# while True:
#     constent=input("请输出你要说的内容：,输入Q退出 ")
#     if constent == "":
#         continue # 停止当前本次循环，继续进行下次循环，不会彻底中断循环
#     if constent == "Q":
#         # 退出程序打断循环
#         break  #直接调出循环
#     else:
#         print("你对打野说：",constent)

# 能够让循环推出的条件：
    # 1、break
    # 2、改变条件
# 先判断 while 后 条件是否为真，若为真，则进行对循环体进行执行；然后再返回至while处，在进行判断
# 以此进行循环

# if True:
#     print("wa ha ha")

# 固定输入次数
# count = 1
# while count <= 3:
#     count = 1
#     content = input("请输入内容：")
#     print("你要说的话：",content)
#     #改变count
#     count = count + 1


# continue 停止当前本次循环，不会终止该次循环，停止本次循环开始下一轮的循环
# break  直接退出循环

# 计算1-100的和
# sum = 0
# count = 0
# while count <= 99:
#     sum =sum + count
#     count = count + 1
#     print("当前数字：",count)
# print(sum)

# 数出1-100内的奇数

# count = 1
# while count <= 100:
#     print("当前数字：",count)
#     count = count + 2

count = 1
while count <= 99:
    if count % 2 == 1:

        print(count)
    #print("当前数字：",count)
    # count = count + 1
count += 1
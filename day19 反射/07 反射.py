import master  # 该处的报错不用管

# print('''
#     1、大牛特别能吃
#     2、大牛特别能喝
#     3、大牛特别能玩
#     4、大牛特别能睡
#     q、推出测试程序
# ''')
#
# while 1:  # 进行反复的测试
#     constent = input("请输入你要执行的函数：")
#
#     if constent == "1":
#         master.chi()
#     elif constent == "2":
#         master.he()
#     elif constent == "3":
#         master.play()
#     elif constent == "4":
#         master.shui()
#     elif constent == "q":
#         print("程序正在退出..........")
#         break
#     else:
#         print("输入序号错误")

# master.chi()
# master.he()
# master.play()
# master.shui()

# 在反向测试时使用

while 1:
    constant = input("请输入你要测试的功能：")  # 用户输入的功能是字符串

    # 反向测试时使用
    # 判断master中是否含有constant ，既可以判断属性，也可以判断方法
    if hasattr(master, constant):
        print("有该功能")
        x = getattr(master, constant)  # 得到master中的constant
        # print(x)  # <function chi at 0x000001DCEDDF5378>
        x()  # 执行该函数
    else:
        print("没有该功能")



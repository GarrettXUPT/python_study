# def chi():
#     print("不吃了")
#
# chi() # 小括号表示调用


# 使用指定的程序，完成或者完不成动作
# def funcyion(reult):
#     # 描述你的动作
#     print("先加到10迈以上")
#     print("换二档")
#     print("再加到大致25的样子")
#     print("语音响起，开始加减档")
#     print("换三档，再加至30多一点，换四档")
#     print("马上调回三挡，再调回二挡")
#     print(f"{reult}动作")
#
# funcyion("完成")
# funcyion("不完成")



# # 实参：位置参数举例，默认参数要放在形参列表的最后
#
# def chi(zhushi,fushi,tiandian):
#     print(f"先吃{zhushi}")
#     print(f"再吃{fushi}")
#     print(f"再来点{tiandian}")
# # chi("大米饭","菜","冰淇淋")
# chi(fushi="大米饭",zhushi="菜",tiandian="冰淇淋")

def regist(name,age,edu,gender="男"): # 默认情况下gender就是男，默认值在不给参数时候起作用，若在使用函数时对默认值进行修改，也是合法的
    print(f"{name}")
    print(f"{age}")
    print(f"{edu}")
    print(f"{gender}")

regist("赵玉吧",12,"硕士","男")
regist("赵云",23,"博士","男")
regist("刘备",22,"皇叔")
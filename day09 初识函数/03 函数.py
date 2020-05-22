# 可以使用函数来定义一个动作，
# def funcyion():
#     # 描述你的动作
#     print("先加到10迈以上")
#     print("换二档")
#     print("再加到大致25的样子")
#     print("语音响起，开始加减档")
#     print("换三档，再加至30多一点，换四档")
#     print("马上调回三挡，再调回二挡")
#     print("完成动作")
#
# # 调用函数
# # funcyion()
# print(funcyion()) # None 没有返回值
# print(funcyion)  # function funcyion at 0x0000022ABA0FD1E0> 该描述为函数存在的内存地址，内存地址中存储着功能代码


# def funcyion():
#     # 描述你的动作
#     print("先加到10迈以上")
#     print("换二档")
#     print("再加到大致25的样子")
#     print("语音响起，开始加减档")
#     print("换三档，再加至30多一点，换四档")
#     print("马上调回三挡，再调回二挡")
#     print("完成动作")
#     # 得到一个结果
#     # return "该死的科三"  # 带着返回值的函数
#     return "该死的科三","不想练啊","好烦"  # 同时返回多个结果
# s = funcyion()  # 该处调用函数，返回值就返回到这里，哪里调用，就返回哪里
# # print(s)  # 该死的科三
# print(s) # 返回多个结果，则返回的是元祖，将多个返回结果聚合成为元组 ('该死的科三', '不想练啊', '好烦')



# 函数的返回值问题：
#   1、函数可以有返回值，也可以没有返回值
#   2、函数如果没有返回值，则在其执行完毕以后，默认返回None
#   3、在函数中只写了return，但是没有写返回值,返回的是None，后面的就不再执行
#   4、在函数后段手动返回None，则与返回None的情况相同，这个None写和不写都一样
#   5、在函数最后返回一个值，那么就返回一个结果，若返回多个值，则返回元组

# def funcyion():
#     # 描述你的动作
#     print("先加到10迈以上")
#     print("换二档")
#     print("再加到大致25的样子")
#     print("语音响起，开始加减档")
#     print("换三档，再加至30多一点，换四档")
#     print("马上调回三挡，再调回二挡")
#     print("完成动作")

# # 练习：写一个函数，在函数内部，需要用户输入两个数，返回较大的那个数
# def fuction():
#     a = input("请输入一个数字：")
#     b = input("再输入一个数字：")
#     if a > b:
#         # print(a)
#         i = a
#     else:
#         # print(b)
#         i = b
#     return i
# s = fuction()
# print(s)

# 简单写法
def fuction():
    a = input("请输入一个数字：")
    b = input("再输入一个数字：")
    # if a > b:
    #     return a
    # else:
    #     return b
    # 三目运算
    c = a if a > b else b
    return c
s = fuction()
print(s)
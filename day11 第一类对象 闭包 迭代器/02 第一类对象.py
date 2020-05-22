# def fu():
#     print("我叫fn")
#
# print(fu) # <function fu at 0x000001A377CCC1E0>
# fu()  # 我叫fn
#
# gn = fu # 函数名可以进行赋值  直接将地址传递给gu，gn与fu共同指向同一个函数,相当于浅拷贝
#
# print(gn) # <function fu at 0x000002AF547AC1E0>
# gn()  # 我叫fn

# def func1():
#     print("hello")
#
# def func2():
#     print("nice to meet you")
#
# def func3():
#     print("oh for god sake")
#
# def func4():
#     print("it is not help that")
#
# lst = [func1,func2,func3,func4]
#
# # print(lst) # 显示函数位置，并没有进行调用 [<function func1 at 0x000002B91593C1E0>,
# #             # <function func2 at 0x000002B915C76378>, <function func3 at 0x000002B916CEAB70>,
# #                 # <function func4 at 0x000002B916CEABF8>]
# # # 调用
# # lst[0]() # hello
# # 将其中每一个函数都进行循环
# for el in lst: # el 为列表中的每一项
#     el() # hello
#         # nice to meet you
#         # oh fr god sake
#         # it is not help that

# def wrapper():
#     def inner():
#         print("还可以这样写")
#     print(inner)
#     return inner
#
# ret = wrapper() # <function wrapper.<locals>.inner at 0x0000024FFB566378>
# print(ret) # <function wrapper.<locals>.inner at 0x0000024FFB566378>


# def wrapper():
#     def inner():
#         print("你好")
#     return inner() # 函数名可以像返回值一样返回
#
# ret = wrapper()
# # ret()  # 你好
# # # 在函数外，访问内部函数
#
# def func1():
#     a = 10
#     return a
# print(func1())  # 10

def fuunc1():
    print("im here")
# 代理
def proc(a):  # 充当调用函数,函数也可作为参数，进行传入
    print("我是代理")
    a()
    print("代理结束")
proc(fuunc1) # im here 我是代理
            # im here
            # 代理结束

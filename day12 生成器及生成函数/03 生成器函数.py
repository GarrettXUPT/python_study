# def func():
#     print("你好")
#     return "好什么好，有多好" # 在函数中表示返回的意思
#
# ret = func()
# print(f"返回值是：{ret}")


# def func():
#     print("你好")
#     yield  "好什么好，有多好" # yield表示返回 但不会终止函数的执行
#     print("不太好")
#     yield "那你刚才啥意思"
# ret = func()  # 执行函数
# print(f"返回值是：{ret}") # 返回值是：<generator object func at 0x000002078C7E94F8>
#
# # next 执行到下一个yield
# print(ret.__next__()) # 第一次执行next 此时程序才开始运行
# print(ret.__next__()) # 执行到下一个yield，已经执行到了yield
# 你好
# 好什么好，有多好

# 不太好
# 那你刚才啥意思

# 买衣服 10000

# def buy():
#     lst = []
#     for i in range(1,10001):
#         lst.append("衣服%s" % i)
#     return lst
#
# lst = buy()
# print(lst)


# def buy():
#     for i in range(1,10001):
#         yield "衣服%s" % i
#
# gen = buy() # 得到的是生成器函数,生成器或者迭代器的好处就是节省内存
# # print(gen.__next__())
# # print(gen.__next__())
# # print(gen.__next__())
#
# # 迭代器意味着可以使用for循环
# # for yifu in gen:
# #     print(yifu)
#
# lst = list(gen) #在list内部使用的是for循环
# print(lst) # 此时生成的就是一个大列表

# send() -》 与__next__（）相同 但send可以给上一个yield位置传值

def func1():
    print("韭菜盒子")
    a = yield "韭菜鸡蛋"
    print("a",a)
    b = yield "韭菜西红柿"
    print("b",b)
    c = yield "火烧"
    print("c",c)

gen = func1()

print(gen.__next__())  # 执行完第一个yield
print(gen.send("篮球"))  # 表示执行到下一个yield
# print(gen.__next__())  # 从第一个yield开始，执行完第二个yield


# print(gen.__next__())
# 韭菜盒子
# 韭菜鸡蛋

# print(gen.send("篮球"))
# 韭菜盒子
# 韭菜鸡蛋
# a 篮球
# 韭菜西红柿

# print(gen.send("足球"))
# 韭菜盒子
# # 韭菜鸡蛋
# # a 篮球
# # 韭菜西红柿
# # b 足球
# # 火烧
# print(gen.__next__())

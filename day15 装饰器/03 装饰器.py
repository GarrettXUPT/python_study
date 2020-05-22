# def zaoren():
#     # print("浇点水") # 该需求 有的时候需要 有的时候不需要
#     print("捏个泥人")
#     print("吹口仙气")
#     print("你就出来了")
#
# # zaoren()
# # zaoren()
# # zaoren()
#
# # 三年大焊 没有水
# def water():
#     print("浇水")
#     zaoren()
# # 此时的设计就不符合开闭原则
# water()

# 装饰器
# 在原函数开始之前和做完之后，加入一些新的功能
# 在不影响原用户的使用基础上 加入一些新的功能，在目标函数之前和之后插入一些新的代码，并且不改变原来的代码
# def warpper(fn): # fn接受的是一个函数
#     def inner():
#       print("浇水")
#       fn() # 调用进来的函数
#     return inner
#
# def zhishu():
#     print("栽树")
#
# def zaoren():
#     # print("浇点水") # 该需求 有的时候需要 有的时候不需要
#     print("捏个泥人")
#     print("吹口仙气")
#     print("你就出来了")
#
# zaoren = warpper(zaoren)
# zaoren()
#
# zhishu = warpper(zhishu)
# zhishu()


# # 装饰器的深入
# def play(usename,password):
#     print("点击lol",usename,password)
#     print("选择人物")
#     print("释放技能")
#     return "斩杀地将"
#
# def kxxxl(qq_number):
#     print("开心消消乐",qq_number)
#     print("开心消消乐")
#     print("开心消消乐")
#
def wrapper(fn):
    def inner(*args, **kwargs): # 无敌传参，接收到的是元组（"alex","123"）
        print("开挂")
        ret = fn(*args, **kwargs) # 接受到的所有的参数，打散传递给正常的参数
        print("关闭开挂")
        return ret
    return inner
#
# play = wrapper(play)
# ret = play("alex","123") # 此时play对应的是inner play = inner
#
# print(ret)
#
# kxxxl = wrapper(kxxxl)
# kxxxl(12345)


# 通用装饰器写法
# python 里面的动态代理   
# 装饰器存在的意义：在不破坏原有函数和原有函数调用的基础上，给函数添加新的功能
def warpper(fn):  # 此时fn是目标函数
    def inner(*args,**kwargs): # 为了目标函数传参
        '''在执行目标函数之前需要添加的代码'''
        ret = fn(*args,**kwargs) # 调用目标函数,ret 是目标函数的返回值
        '''在执行目标函数之后需要添加的代码'''
        return ret # 将目标函数返回值返回，保证函数正常的结束
    return inner

@warpper # target_func = warpper(target_func) # 此时fn就是target_func
def target_func():
    pass

# target_func = warpper(target_func) # 此时fn就是target_func
target_func() # 此时执行的是inner
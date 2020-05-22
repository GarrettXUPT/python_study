# a = 10
# c = str(a) # 将数字转化为字符串
# print(type(c)) # <class 'str'>
#
# b = "20"
# print((type(b))) # <class 'str'>
#
# print(type(int(b))) # <class 'int'> , 将字符串转化为数字

# 字符串 ==》 数字 int（）
# 数字 ==》 字符串 str（）
# x ==》 y类型 y(x)

# 结论一：想把xxx数据转化为yyy类型的数据，yy（）

# 数字转化为bool
# 在bool中 只有0 为false 非0都为True；

# 将字符串转化为布尔
# 在bool中 只有空字符串为False，其他都为 True

# a = 10
# b = bool(10)
# print(b)# True
# print(type(b)) #<class 'bool'>
# c = "haha"
# d = bool(c)
# e = ""
# f = bool(e)
# print(d) # True,空格为True
# print(f) # False

# 结论二：所有的空都可以表示False

# print(bool([""])) #空列表，表示False
# print(bool(tuple())) # 空元组也为False
# print(bool({})) # 空字典也为False

# None 表示 空
# print(bool(None)) # False
while 1: #从运行效率来讲， while 1 ： 要比while True：更高一点，因为省去了将True转化为数字1
    print("gun")
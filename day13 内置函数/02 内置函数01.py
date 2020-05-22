
# lst = ["今天星期三","明天星期四","你四不四傻"]
# # it = lst.__iter__()
# it = iter(lst)
# print(it)
# print(next(it)) # print(it.__next__())
# print(next(it)) # print(it.__next__())
# print(next(it)) # print(it.__next__())

# print("你好，我是Garrett",end = " ") 结尾添加一个空格
# print("你好，我叫walker") # 你好，我是Garrett 你好，我叫walker
#
# print("包浪","女神","好烦","算了",sep="") # 包浪女神好烦算了 sep 表示分隔符，默认是空格

# hash算法，最后出来的一定是数字
# 数字算出来就是数字本身，其他的数据算出来是一串很长的数字
# print(hash("你好")) # -4246181796394750372
#
# # id()查看内存地址
# print(id("hehe")) # 2562982569832

# re = __import__(input("请输入你要导入的模块：")) # 动态导入模块
# re.search()


# print(help(str)) # 查看某函数帮助文档，尤其是在高级框架中较为常见

# callable 判断函数是否是可调用的

# def func():
#     pass
#
# a = 18
# print(callable(func)) # True 表示可调用 func() 表示调用 实际上是在判断函数名是否可以加括号调用
# print(callable(a)) # False 不可调用
#
# # dir() 查看括号内对象有哪些操作 ，此类型数据可以执行哪些方法


# complex 表示复数 = 实部 + i虚部
# 专业的东西去做专业的事

# # 进制转换
# print(bin(12)) # bin() 将数字转化为二进制数 0b1100
# print(hex(23)) # hex() 将数字转化为十六进制 0x17
# print(oct(12)) # oct() 将数字转化为八进制 0o14

# # 下属函数中必须写入可迭代对象
# print(sum([1,2,3,4])) # 10
# print(min([1,2,3,4])) # 1
# print(max([1,2,3,4])) # 4

# print(divmod(10,3)) # （3,1) divmod 计算10/3的商和余数，返回的是一个元组
#
# print(round(1.5)) # 2
# print(round(1.4)) # 1
# print(round(2.4)) # 2
# print(round(2.5)) # 2  整数部分是奇数——>正常四舍五入 如果整数部分是偶数——>五舍六入
#
# print(pow(2,3))  # 表示求幂 2**3

# lst = ["篮球","足球","排球"]
# for el in lst: # 查看列表中元素
#     print(el)
#
# for i in range(len(lst)): # 查看元素索引值
#     print(i,lst[i])
#
# # enumerate(lst,100) 从100 开始计索引值
# for element in enumerate(lst):
#     print(element)
# # (0, '篮球')
# # (1, '足球')
# # (2, '排球')
#
# for i,el in enumerate(lst):
#     print(i,el)
# # 0 篮球
# # 1 足球
# # 2 排球

# print(all([1,2,"haha"])) # True all 表示的含义是and
# print(any([1,2,0])) # True 表示的含义是 or

# zip 拉链函数
lst1 = ["赵四","刘能","王长贵"]
lst2 = ["刘小光","王小利","不清楚"]
lst3 = ["街舞","磕巴","哭"]

z = zip(lst1, lst2, lst3)  # 将对应元素聚合为一个列表,返回聚合以后的数组，但是原数组就变为元组类型，聚合后是三个元素的数组
print(z)
print("__iter__"in dir(z)) # True 判断是否为可迭代对象
for el in z:
    print(el)
# ('赵四', '刘小光', '街舞')
# ('刘能', '王小利', '磕巴')
# ('王长贵', '不清楚', '哭')
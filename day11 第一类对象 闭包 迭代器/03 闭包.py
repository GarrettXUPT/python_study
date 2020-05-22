# 闭包的优点：
#    1、保护其变量不被他人侵害
#    2、保持一个变量常驻内存，加快调用速度

# 全局变量是不安全的定义方式
def wrapper():
    name = "周杰伦"
    def inner():
        print(name)
    # inner() # 内层函数被调用，使用的是外层函数的局部变量
    return inner # 返回函数名
ret = wrapper()
# ret() # 周杰伦
print(ret.__name__) # 显示执行的函数真实的名字 inner


# def wrapper():
#     name = "周杰伦" # 将局部变量常住于内存
#     def inner():
#         print(name)
#     return inner
#
# ret = wrapper() # ret是一个内层函数
# print("这里还可以添加代码，执行的时机是不确定的")
#
# ret() # ret是inner，ret执行的时机不确定，所以它必须保证内存里面的name必须存在

# def wrapper():
#     name = " 你好"
#     def inner():
#         print(name) # (<cell at 0x0000024330585498: str object at 0x0000024330578558>,
#     print(inner.__closure__)  # 查看内容是否闭包，有内容就是闭包，没有内容就不是闭包
#     # 你好
#     inner()
#     return inner
#
# wrapper()
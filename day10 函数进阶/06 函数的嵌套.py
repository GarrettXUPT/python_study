def outter():
    def inner():
        print("我的天哪")
    inner()
    print("你干啥")

# outter()  # 我的天哪 你干啥
# inner() # 在全局不能找到局部的内容

# a = 10
# def func():
# #     a = a + 10 # 该种方法试图改变全局变量，若此处修改，那么其他函数调用a时，也会发生修改，所以这种操作不合法
# #       若想改变全局变量
#     global a
#     a = a + 10  # 该种方法修改了全局变量，需要注意的是，这种修改方式将全局变量修改，也会影响到其他使用它的函数

# nonlocals() 在局部，寻找离他最近的外层的一个变量，与global的作用相同，只是修改的范围不一样

def func():
    a = 10
    def func1():
        nonlocal a  # 使用该种方法将离他最近的一个变量进行强行引用修改
        a = a + 10
        print(a)

# 如果没有global和nonlocals 我们查找的顺序就是 自己 上一层，再上一层
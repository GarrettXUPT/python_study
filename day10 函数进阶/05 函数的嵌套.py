def func1():
    print("我是func1")

def func2():
        print("我是func1")
        func1()

def func3():
        print("我是func1")

def func4():
        print("我是func1")
        func3()

# 函数的互相调用不是函数的嵌套
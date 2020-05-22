def wrapper1(fn):
    def inner(*args,**kwargs):
        print("1111")
        ret = fn(*args,**kwargs)
        print("2222")
        return ret
    return inner

def wrapper2(fn):
    def inner(*args,**kwargs):
        print("3333")
        ret = fn(*args,**kwargs)
        print("4444")
        return ret
    return inner

def wrapper3(fn):
    def inner(*args,**kwargs):
        print("5555")
        ret = fn(*args,**kwargs)
        print("6666")
        return ret
    return inner

# 就近原则
@wrapper1
@wrapper2
@wrapper3
# wrapper3 最先被装饰，wrapper2装饰的是wrapper3装饰以后的函数，以此类推
def func():
    print("我是可怜的func")

func()
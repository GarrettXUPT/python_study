def wrapper_out(flag): # 装饰器本身的参数
     def wrapper(fn):
        def inner(*args,**kwargs):
            if flag == True:
                print("打探市场")
                ret = fn(*args,**kwargs)
                print("你骗我，恨你")
                return ret
            else:
                ret = fn(*args,**kwargs)
                return ret
        return inner
     return wrapper

@wrapper_out(True) # 执行流程：先执行wrapper_out下代码，返回一个装饰器 再与@做拼接 @装饰器
def yue(s):
    print(f"你好啊{s}")

yue("baoboa")
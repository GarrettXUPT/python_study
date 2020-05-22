# class Foo:
#     def __init__(self):
#         print("初始化，在创建对象的时候自动调用这个方法") # 只有在Foo()时，会自动执行__init__()，也可以重复调用
#
# f = Foo()
# print(callable(f)) # False

# 想要使该对象变得可以被调用，则进行以下操作


class Foo:
    def __init__(self):
        print("初始化，在创建对象的时候自动调用这个方法") # 只有在Foo()时，会自动执行__init__()，也可以重复调用

    # 为了对象可被调用
    def __call__(self, *args, **kwargs):
        print("我可以使对象加括号")

    # 为了给对象[]时，使用
    def __getitem__(self, item):
        print("item = ",item)
        print("我执行了__getitem__()")
        return "haha"

    # 为了给对象[]时，使用
    # 对象[key] = value
    # dic["jay"] = 周杰伦
    def __setitem__(self, key, value):
        print("key",key)
        print("value",value)


f = Foo()
# print(callable(f)) # True
# f() #  调用的是__call__() 我可以使对象加括号


# print(f["李嘉诚"]) # 自动调用__getitem__()
# # item =  李嘉诚
# # # 我执行了__getitem__()
# # haha

f["jay"] = "林俊杰"
# key jay
# # value 林俊杰

# 面向对象的执行流程——>
# 1、加载类 ——> 各类创建名称空间 ——> 主要存放类变量
# 2、创建对象 ——> 先找类 ——> 根据类开辟内存 ——> 执行类中的__new__() ——> 执行__init__()对其进行初始化 ——> 返回对象

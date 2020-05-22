# print(1/0)  # 在程序执行时，产生一个错误对象，系统会抛出这个错误
            # 如果错误没有进行处理，则错误就会显示给用户

# 处理异常：在python中可以通过try....except...来处理错误
# 若错误没有进行处理，则程序就会结束，而不会继续向下执行，若对程序进行了错误处理，则程序还会继续向下运行

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print("出错了，错误是：ZeroDivisionError")
# 出错了，错误是：ZeroDivisionError

# 所有异常的根是Exception，所有的异常类都会默认继承Exception

# try:
#     print(1 / 0)
#     open("哈哈哈",mode="r")
# except Exception:  # Exception 可以处理所有错误
#     print("出错了")
# # 出错了

# # 如果try里面的代码有出错的，则只会报出这一个错误
# try:
#     print(1 / 0)
#     open("hahaha",mode="r")
# except ZeroDivisionError:
#     print("分母不能为0")
# except FileNotFoundError:
#     print("文件找不到")
# except Exception:  # 在处理异常最后，要加上Exception以防有错误没有估计到
#     print("其他错了")
# else:  # 当try中不产生任何错误时，会自动执行else里的代码
#     pass
# finally:  # 最终：不管出错还是不出错，都要执行finally，一般用来进行收尾
#     print("哈哈哈")

# 如何手动抛出异常
# def add(a, b):
#     # 定义智能是数字进行相加
#     if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
#         return print(a + b)
#     else:
#         # 抛出异常
#         # raise 异常类(错误信息)
#         raise Exception("没办法进行处理")
# add(1, 2)
# add("11", 2)  # Exception: 没办法进行处理


# 如何自己定义异常
# 随便写一个类，这个类只要继承了Exception即可 这个类就是异常类 就可以作为raise的对象
# class Cul_Exception(Exception):
#     print("宝宝出错了")
#
#
# def add(a, b):
#     # 定义智能是数字进行相加
#     if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
#         return print(a + b)
#     else:
#         # 抛出异常
#         # raise 异常类(错误信息)
#         raise Cul_Exception("没办法进行处理")
# add(1, 2)
# add("11", 2)  # __main__.Cul_Exception: 没办法进行处理



import traceback # 查看堆栈信息

class Gender_Exception(Exception):
    pass


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def xizao(self):
        print(f"{self.name}在洗澡")


def nan_zao_tangzi(ren):
    if ren.gender == "男":
        ren.xizao()
    else:
        raise Gender_Exception("进错了，去对门看看")  # 抛出异常是很重要的

try:  # 处理异常
    p1 = Person("Garrett","男")
    p2 = Person("walker","女")

    nan_zao_tangzi(p1)
    nan_zao_tangzi(p2)

except Gender_Exception:
    f = traceback.format_exc()
    print(f)
    # Traceback (most recent call last):
    #   File "F:/python_study/day20 约束 异常处理 日志处理/04 异常处理.py", line 90, in <module>
    #     nan_zao_tangzi(p2)
    #   File "F:/python_study/day20 约束 异常处理 日志处理/04 异常处理.py", line 83, in nan_zao_tangzi
    #     raise Gender_Exception("进错了，去对门看看")  # 抛出异常是很重要的
    print("性别错误")

# 错误信息叫做堆栈信息


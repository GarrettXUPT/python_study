# 回忆装饰器

# from functools import wraps  # 可以改变函数的名字和文档的注释
# def wrapper(fn):
#     @wraps(fn)  # 将inner的名字改变为func
#     def inner(*args, **kwargs):
#         print("前")
#         ret = fn(*args, **kwargs)
#         print("后")
#         return ret
#     return inner
#
#
# @wrapper # func = wrapper（func）
# def func():
#     print("hahaha")


#map 映射 reduce 归纳
# map(func, iter) 将后面的可迭代对象，依次送入func进行处理
# print(list(map(lambda x:x**2, [i for i in range(10)])))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# from functools import reduce
#
# def func(a, b):
#     return a + b  # 0 + 1 + 4 + 6 + 7 累加
#
# # 会将每一个数据交给func来执行,会把默认值0作为第一个参数传递给reduce
# # 接下来将刚才返回的结果作为第一个参数，传递给a
# ret = reduce(func, [1,2,4,6,7], 0)
# print(ret)
# print(reduce(lambda x, y:x + y, [i for i in range(101)]))  # 表示0-100的累加结果




# from  functools import partial
#
# def chi(zhushi, fushi):
#     print(zhushi, fushi)
# # 偏函数
# # 固定函数中某些参数的值
#
# chi2 = partial(chi, fushi = "辣鸡爪")
#
# chi2("大米饭")
# chi2("小米饭")
# chi2("黑米饭")
# chi2("糯米饭")

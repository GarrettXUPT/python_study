
# # 写函数，检查获取传入列表或元组对象的所有的奇数位索引对应的元素
# # 并形成新列表返回给调用者
#
# def func(lst):
#     return list(lst[1::2])
#
# print(func([12,33,4,5,6,7,6]))


# # 写函数，判断用户传入的对象（字符串、列表、元组）的长度是否大于5
# def func(s):
#     # if len(s) > 5:
#     #     return True
#     # else:
#     #     return False
#     return len(s) > 5
# print(func("哈哈"))  # False


# # 写函数，检查传入列表长度，如果大于2，则将列表的前两项内容返回给调用者
# def fuc(lst):
#     if len(lst) > 2:
#         return lst[0:2]   # lst[0],lst[1]，左闭右开区间
# print(fuc([1,2,3,45,6]))  # [1, 2]


# # 写函数，计算传入的函数串中，数字，字母，数字以及其他内容的个数，并返回结果
# def fuc(s=""):
#     for c in s:
#         shuzi = 0
#         zimu = 0
#         kongge = 0
#         qita = 0
#         if c.isdigit():
#             shuzi = shuzi + 1
#         elif c.isalpha():
#             zimu = zimu + 1
#         elif c == " " :
#             kongge = kongge + 1
#         else:
#             qita = qita + 1
#     return shuzi , zimu , kongge , qita
#
# # 写函数，接收两个参数，返回值比较大的那个数字
# 接收参数，不用管参数从哪里来
# def func(a,b):
#     return a if a > b else b



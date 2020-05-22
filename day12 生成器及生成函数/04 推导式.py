# 生成列表 python s1 -> s18
# lst = []
# for i in range(1,19):
#     lst.append(i)
# print(lst)

# 列表推导式 [结果 for循环 if条件]

# lst = ["python %s期" % i for i in range(1,19)]
#
# print(lst)
#

# # # 生成列表中含有1-100之间所有偶数的平方
# lst = []
# for i in range(1,101):
#     if i % 2 == 0:
#         lst.append(i**2)
# print(lst)
#
# lst1 = [i**2 for i in range(1,101) if i % 2 == 0]
# print(lst1)

# # 筛选出列表中姓张的同学
#
# lst = ["张无忌","周自若","反正","你猜猜"]
#
# lst2 = [name for name in lst if name.startswith("张")]
#
# print(lst2)

# # 寻找名字中带有两个e的名字
# name = [["tom","billy","ieee","walker"],["garrett","ieef","ceef"]]
# lst = []
# for name1 in name:
#     for name2 in name1:
#         if name2.count("e") == 2:  # 若名字中有两个e name.count("Ga") 表示若姓名中带有Ga的人
#             lst.append(name2)
# print(lst)

# 字典推导式
# 语法 {结果{key：value} for 循环 if 条件}

# lst = [11,22,33]
#
# dic = {i:lst[i] for i in range(len(lst))}
#
# print(dic) # {0: 11, 1: 22, 2: 33}

# # 练习 {"主食":"米饭","副食":"小拌菜","汤":"疙瘩汤"} 将key与value互换 生成了新的字典
#
# dic = {"主食":"米饭","副食":"小拌菜","汤":"疙瘩汤"}
#
# d = {v:k for k,v in dic.items()}
# dic.items() 返回值是字典的键值对的迭代对象
# print(d)

# 集合推导式
# 语法{k for循环 if 条件}

# 没有元组推导式
g = (i for i in range(1,101)) # 生成器表达式

print(g) # <generator object <genexpr> at 0x000001BE3AD494F8>
print(g.__next__()) # 1

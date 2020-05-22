
# lst = ["alex","dsb","wusir","xsb"]
# # s = "_".join(lst) # join 是字符串的一个操作,使用前面的字符串，对后面的列表进行拼接，拼接的结果是一个字符串
# # 
# # # 与split（）相对应，split是根据你给的参数进行切割，切割的结果 是列表
# # s1 = "alex_dsb_wusir_xsb"
# # lst1 = s1.split("_")   # 可以存储多种数据类型的列表，不可能会是元组，因为元组不可变
# # 该切分操作以后得到的是列表
# # print(lst1) # ['alex', 'dsb', 'wusir', 'xsb']
# # print(s) # alex_dsb_wusir_xsb
# #
# # # 需要把字符串变成列表：split（）
# # # 把列表转化为字符串 join（）

# print("*".join("周润发"))  # 周*润*发 使用迭代的方式依次进行拼接


# 2、关于删除
# lst = ["篮球","足球","乒乓球","排球"]
#
# # 请空列表 lst.clear()
# for el in lst:  # 使用该种方式删除时候，会出现后项元素向前顶位，删除点向后移位，会出现空档而造成漏删
#     lst.remove(el)
# print(lst) # []
#
# for i in range(len(lst)):
#     lst.pop() # 按索引进行删除，默认删除最后一个
# print(lst) # []

# lst = ["篮球","足球","乒乓球","排球","电子竞技"]
# # 最合理的删除方式：
# # 1、把要删除的内容写在新列表中
# # 2、循环新列表，删除老列表
#
# # 需求：删除列表中带球字的元素
# new_list = []
# for el in lst:
#     if "球" in el:
#         new_list.append(el) # 记录要删除的内容
# for el in new_list:
#     lst.remove(el)
# print(lst)  # ['电子竞技']

# # 字典
# # 字典在循环的时候是不能被删除的，删除可能会导致底层结构的混乱
dic = {"张无忌":"乾坤大挪移","周芷若":"哭","赵敏":"卖萌"}
#
# # for key in dic:
# #     # dic.pop(key)
# #     dic["灭绝师太"] = "倚天剑"
# # print(dic)
#
# # 把要删除的key保存在一个新的列表中，循环该列表，删除字典中的元素
lst = []
for i in dic.keys():
    lst.append(i)
print(lst)  # ['张无忌', '周芷若', '赵敏']
for el in lst:
    dic.pop(el)
print(dic)  # {}

# # 坑：fromkeys（）帮助创建字典

# # 把第一个参数进行迭代，拿到每一项的key和后面的value组合成为字典
# d = dict.fromkeys("张无忌","赵敏")
# # dic = {}
# # print(type(dic))
# print(d)  # {'张': '赵敏', '无': '赵敏', '忌': '赵敏'}


# # 坑1：返回新字典，与原来字典没有关系
# dic = {}
# d = dict.fromkeys("张无忌", "赵敏")
# print(dic) # {}
# print(d) # {'张': '赵敏', '无': '赵敏', '忌': '赵敏'}
#
# # 坑2：若value是可变数据类型
# d = dict.fromkeys("张无忌",[])
# print(d)
# d['张'].append("河南特色")
# print(d) # {'张': ['河南特色'], '无': ['河南特色'], '忌': ['河南特色']}
# # 张无忌三个key对应的列表是同一个，所以，一个修改则全部修改

# # 删除集合，数着新列表，删除旧集合
# s = {"杨潇","韦一笑","谢逊","楚留香"}
# lst = []
# for i in s:
#     lst.append(i)
# for el in lst:
#     s.remove(el)
# print(s)  # set()


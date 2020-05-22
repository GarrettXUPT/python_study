# dic = {"jay":"周杰伦", "jj":"林俊杰", "jolin":"蔡依林"}
# for key in dic:
#     print(key) # 得到key
#     print(dic[key]) # 得到value

# dic = {"jay":"周杰伦", "jj":"林俊杰", "jolin":"蔡依林"}
# print(dic.keys()) # dict_keys(['jay', 'jj', 'jolin']) 像列表
# for k in dic.keys():
#     print(k)  # 拿到字典中的每一个key
#
# # 当需要单独获取value时 使用values
# print(dic.values())
# for v in dic.values():
#     print(v)

# dic = {"jay":"周杰伦","jj":"林俊杰","jolin":"蔡依林"}
#
# # print(dic.items()) # 得到所有的键值对，dict_items([('jay', '周杰伦'), ('jj', '林俊杰'), ('jolin', '蔡依林')])，以元组的形式，放入列表中
#
# # for item in dic.items():
# for k,v in dic.items():
#     #print(item)
# # ('jay', '周杰伦')
# # ('jj', '林俊杰')
# # ('jolin', '蔡依林')
# #     k = item[0]
# #     v = item[1]
#     k,v = item # 将item直接解构
#     print(k,v)
# #
# # # jay 周杰伦
# # # jj 林俊杰
# # # jolin 蔡依林
#
# # a,b = 1,2 # 将后面的两个值分别赋值给前面的两个变量，称之为 解构，解包
#
# # 元素和列表是可以解包的
#
# # d,e,f = (1,2,3)
# # print(d,e,f) # 1 2 3



# 遍历字典的两套方案

# 1.使用for 循环 直接遍历字典的key
dic = {"jay":"周杰伦","jj":"林俊杰","jolin":"蔡依林"}
for key in dic:
    print(key,dic[key])
# jay 周杰伦
# jj 林俊杰
# jolin 蔡依林

# 2、直接使用items（）和解构，直接获取key和value
for k,v in dic.items():
    print(k,v)
# jay 周杰伦
# jj 林俊杰
# jolin 蔡依林

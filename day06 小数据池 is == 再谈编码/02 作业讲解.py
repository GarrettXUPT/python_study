# dic = {'k1':"v1","k2":"v2","k3":[11,22,33]}

# # 循环输出所有的key
# for key in dic.keys():
#     print(key)
# # 循环输出所有的value
# for value in dic.values():
#     print(value)
# # 循环输出所有的key和value
# for k,v in dic.items():
#     print(k,v)

# # 请在字典中添加一对键值对k4，v4
# dic["k4"] = "v4"
# print(dic)
# # 请将k1的value换为walker
# dic["k1"] = "walker"
# print(dic)
    # # 在k3的列表中添加元素44
    # dic["k3"].append(44)
    # print(dic)
# # 在k3第一个元素插入18
# dic["k3"].insert(0,18)
# print(dic)


# # 有如下值li = [11,22,33,44,55,66,77,88,99,90]
# # 将大于66的保存在字典key1中，将小于66的保存于字典key2中
#
# li = [11,22,33,44,55,66,77,88,99,90]
# dic = {"key1":[],"key2":[]}
# for item in li:
#     if item >= 66:
#         dic["key1"].append(item)
#     if item < 66:
#         dic["key2"].append(item)
# print(dic)

# goods = [{"name":"电脑","price":"1999"},
#          {"name":"鼠标","price":"19"},
#          {"name":"游艇","price":"999"},
#          {"name":"美女","price":"199"}]
# for i in range(len(goods)):
#     good = goods[i] # {"name":"电脑","price":"1999"}
#     print(i,good['name'],good['price'])
#
# while 1:
#     content = input("请输入你要商品的序号：")
#     if not content.isdigit() or int(content) > 4:
#         print("您输入的内容不合法")
#     else:
#         num = int(content)
#         # 还原索引
#         index =num - 1
#         good = goods[index]
#         print(f"您要购买的商品名称是：{good['name']}",f"商品的价格{good['price']}")
#         break
# # 请输入你要商品的序号：5
# # 您输入的内容不合法
# # 请输入你要商品的序号：4
# # 您要购买的商品名称是：美女 商品的价格199


# 36 选 7 不可以重复，所以使用集合，要7个随机数，不确定循环多少次
from random import randint

s = set()
while len(s) < 7:
    num = randint(1, 36)
    s.add(num)
print(s)

# for 确定循环的范围，各种遍历
# while 不确定循环次数
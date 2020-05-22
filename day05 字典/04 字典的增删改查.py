
# dic = {"jay":"周杰伦","jj":"林俊杰","jolin":"蔡依林"}
#
# # dic["walker"] = "诗雨"  # 新key表示添加 # {'jay': '周杰伦', 'jj': '林俊杰', 'jolin': '蔡依林', 'walker': '诗雨'}
#
# # dic["jay"] = "诗雨"  # 老key表示替换  # {'jay': '诗雨', 'jj': '林俊杰', 'jolin': '蔡依林'}
#
# # setdefault (难点）
# # 第一个功能是添加，如果前面的key是存在的，那么他什么都不执行
# # 执行流程：判断你给定的key是否在字典中已经存在了，如果不存在则进行添加操作
# dic.setdefault("印度","三傻大闹宝莱坞") # {'jay': '周杰伦', 'jj': '林俊杰', 'jolin': '蔡依林', '印度': '三傻大闹宝莱坞'}
# print(dic)

# dic = {"jay":"周杰伦", "jj":"林俊杰", "jolin":"蔡依林"}
#
# # dic.pop("jay")  # {'jj': '林俊杰', 'jolin': '蔡依林'}
# # dic.popitem() # 删除最后一项，在python的早期版本，字典是无序的 {'jay': '周杰伦', 'jj': '林俊杰'}
# del dic["jj"]  # 删除字典中的特定一项 {'jay': '周杰伦', 'jolin': '蔡依林'}
# dic.clear() # 请空字典
# print(dic)  {}

# dic1 = {"jay":"周杰伦","jj":"林俊杰","jolin":"蔡依林"}
# # dic2 = {"赵四":"刘小光","刘能":"王小利","王木生":"范伟","jay":"周杰"}
# #
# # dic1.update(dic2)
# # # 把dic2的内容更新到dic1中，即将dic2中的内容添加到dic1中
# # print(dic1) # {'jay': '周杰', 'jj': '林俊杰', 'jolin': '蔡依林', '赵四': '刘小光', '刘能': '王小利', '王木生': '范伟'}
# # print(dic2) # {'赵四': '刘小光', '刘能': '王小利', '王木生': '范伟', 'jay': '周杰'}

# 字典的查询
dic = {"jay":"周杰伦","jj":"林俊杰","jolin":"蔡依林"}
# # 直接使用key就可以得到value
# print(dic["jay"]) # 周杰伦,若查询字典中没有的key，则会报错
# # 使用get（key）
# print(dic.get("jay")) # 周杰伦,与直接查询相同，当key不存在 则会返回None，也会马上进行报错
# print(dic.get("jayy", "不存在这个人")) # 不存在这个人  若给定的key不存在则返回后面的参数“这个人不存在”，而不会直接报错
# 使用setdefault（）# 第一个功能是添加，第二个功能是查询，若查到，则不执行任何操作，若没有查到，就执行添加操作
# 整个执行流程：判断给定的key值是否存在，若存在，则不执行新增流程，直接查询出，这个key对应的value
              # 若不存在，则执行新增操作，新增完以后，把对应的value查询出来

dic.setdefault("walker", "诗雨")
ret = dic.setdefault("walker","诗雨")
print(dic)  # {'jay': '周杰伦', 'jj': '林俊杰', 'jolin': '蔡依林', 'walker': '诗雨'}
print(ret) # 获得该元素的value值 诗雨
from collections import Counter

# 计算每个字出现的次数
# print(Counter("宝宝今年多大了"))

# 对可迭代对象的迭代计数，对于整个字典没有办法进行计数，但是可对key和value分别计数
lst = ["jay", "jay", "jay", "宝宝", "宝宝", "胡辣汤", "上官婉儿", "上官婉儿"]
# 对列表内容进行计数，将结果以字典形式呈现，可使用get得到某一个
# print(Counter(lst))  # Counter({'jay': 3, '宝宝': 2, '上官婉儿': 2, '胡辣汤': 1})
c = Counter(lst)
print(c.get("宝宝"))  # 查看宝宝出现的次数
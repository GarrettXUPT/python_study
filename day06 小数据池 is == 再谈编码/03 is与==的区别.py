#         == 比较的是数据值是否相同
#         is 比较的是内存地址是否相同
# lst1 = [1,2,3]
# lst2 = [1,2,3]
# print(id(lst1),id(lst2))
# # 列表没有小数据值
# # 2043483087432 2043483087496
# print(lst1 == lst2) # True
# print(lst1 is lst2) # False

s1 = "周润发"
s2 = "周润发"  # 字符串会被保存在全局常量区，所以内存中只有一个字符串，所以两个指针都指向一个字符串，地址相同
print(id(s1),id(s2))  # 俩地址相同
print(s1 == s2) # True
print(s1 is s2) # True
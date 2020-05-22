# print(tuple("胡辣汤")) # ('胡', '辣', '汤') 元组迭代输出
#
# lst = ["河南话","陕西话","山东话","上海话"]
# r = reversed(lst) # reversed返回的是迭代器
# print(r) # <list_reverseiterator object at 0x000001D875F46780>
# print(list(r)) # ['上海话', '山东话', '陕西话', '河南话']
#
# s = "你好"
# s1 = s.center(20) # 将字符串拉长至20
# print(s1) #    你好

# print(format(3,'b'))  # 11 将3转化为二进制,转化以后的结果是字符串
# print(format(97,'c')) # a 将97转化为unicode类型
# print(format(11,'d')) # 11 将11转化为11
# print(format(11,'o')) # 13 将11转化为八进制
# print(format(11,'x')) # b 将11转化为16进制,若将x化为大写的X，则打印出来是大写的B

print(ord("中")) # 20013 中字在编码的位置是20013
print(chr(20013)) # 中 输入其码位，得到对应的汉字是什么

print(ascii('中')) # 中 转化为unicode码显示的效果，可以用来判断所给信息是否是ascii码中的内容，若输入数据与输出数据一致，则说明该数据就是ASCII码的内容

# 转义字符
# \n 换行 \t tab 制表符 \r 回车 \" 表示双引号
repr() # 还原字符串最官方的效果

# str python的字符串 repr 是通用的字符串
# print(3 != 3)
# #print(3 <> 3) 老版不等于
#
# a = 10
# b = 20
#
# a += b  # a = a + b 累加 sum = sum + count  sum += count
#         # a *= b a = a * b
#         # a //= b  a= a // b
# print(a)
# print(b)
'''
and : 并且 左右两端同时为真 结果才能是真 与

or ： 或者 左右两端有一个是真 结果才能是真 或

not ：非 非真即假 ，非假即真 非
'''

# print(not 5 > 6)

# 当出现混合运算时，需要注意其运算顺序：（）、not 、and 、or ，当出现相同运算时候 从左往右依次运算

# 当出现print( x or y ) 的时候，判断 x 是否为 0 ，如果x == 0 then y ，否则返回 x

# print(1 or 2) 1
# print(0 or 2) 2

# 当出现 print（x and y ）的时候，判断x是否是非 0 ，和 or 相反

# print(1 and 2) 2 # 可先求 1 or 2 然后再取反 2
# print(2 and 3) 3
# print(2 and 0) 0
# print(0 and 1) 0

# 成员运算
# content = input("请输入你的评论：")
#
# if "马化腾" in content: # 你的content是否包含了什么内容
#     print("你的评论不合法")
# else:
#     print(content)

ad = input("请输入你的广告：")
if "最" in ad or "第一" in ad or "全球" in ad:
    print("你的广告不合法！")
else:
    print(ad)
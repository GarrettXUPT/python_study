# # 使每次打印出来的字符串都加上sb
#
# s = "niaosiashi"
# print("sb" + s)
#
# s1 = "321"
#
# for c in s1:
# 	print(f"倒计时{c}秒")
# else:  # 当for循环结束后，自动执行else
# 	print("出发")

# # 实现加法计算器
# content = input("请输入计算内容：") # 5 + 9  split() "5" "9"
# # 字符串的切割
# lst = content.split("+") # 字符串被分割后存入列表，再由列表索引取出对应值，做运算
# # 获取其中的两个数
# # a = int(lst[0])
# # b = int(lst[1])
# # print(f"计算结果{a + b}")
#
# # 多个数相加
# sum = 0
# for el in lst: # 可以使用for循环遍历列表，师列表内的元素相加求和
# 	sum = sum + int(el)
# print(sum)

# 判断内容中有多少个数字
count = 0
content = input("请输入内容：")
for c in content:
	if c.isdigit():
		count = count + 1
print(count)

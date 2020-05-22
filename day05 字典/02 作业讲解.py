
# li = ["alex","walker","frank","crazy","linux"]
# li.extend(["what","why"])  # ['alex', 'walker', 'frank', 'crazy', 'linux', 'what', 'why']
# print(li)

# li = ["干嘛","你说","你不说","我就","走了"]
# content = input("请输入你的评论内容：")
# for el in li:  # el 中为每一个敏感词
#     if el in content: # 判断是否包含敏感词
#         content = content.replace(el, "*"*len(el)) # 替换敏感词为*
# print(content)

# lst = [1, 3, 4,"alex", "taibai", [3,5,6,"nigansha"], 1, "duzijun"]
# for el in lst:
#     if type(el) == list:
#         for item in el:
#             print(str(item).lower())
#     else:
#         print(str(el).lower())

# # 录入学生成绩
# lst = []
# while 1:
#     content = input("请输入信息：以“Q”退出：")
#     if content.upper() == "Q":
#         break
#     else:
#         lst.append(content)
#         print(lst)
# # 并求平均值
# sum = 0
# for item in lst:
#     sum = sum + int(item.split("_")[1])
# avg = sum/len(lst)

# 敲七

i = int(input("输入一个数字："))
lst = []
for num in range(1,i):
    if num % 7 == 0 or "7" in str(num):
        lst.append("duang")
    else:
        lst.append(num)
print(lst)


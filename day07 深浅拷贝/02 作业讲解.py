# # 将评委的打分情况保存到列表中
#
# judge = ["walker","gratte","alex","wusir"]
#
# lst = []
# index = 0
#
# while index < len(judge):
#     fen = input(f"请{judge[index]}打分")
#     if fen.isdigit():
#         fen = int(fen)
#         if fen >= 5 and fen <= 10:
#            lst.append(fen)
#            index = index + 1
#         else:
#             print("分数不合法")
#     else:
#         print("输入分数不正确")
# print(lst)


# 发音
dic = {"1":"yi","2":"er","3":"san","4":"si","5":"wu","6":"liu","7":"qi","8":"ba","9":"jiu","0":"ling",".":"dian"}

content = input("请输入数字：")
# 获取到字符串中的每一个字符
for c in content:
    print(dic[c],end = " ")  # yi er san 
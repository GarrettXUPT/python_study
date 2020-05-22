
# # 判断一个数是否是水仙花数，水仙花数为一个三位数，每一位的三次方的和仍然等于该数，那么这个数就是水仙花数。153 = 1**3+5**3+3**3
# while 1:
#    #  num_input = int(input("请输入要判断的数："))
#     num_input = input("请输入要判断的数：")
#     content = int(num_input)
#     count = 0
#     num = 0
#     while content > 0:  # 判断输入数字的位数
#         content = content // 10
#         count = count + 1 # 通过该种方式对数字位数进行计数
#     if count == 3:
#         # hur = num_input // 100
#         # mid = num_input % 100
#         # dec = mid // 10
#         # sig = mid % 10
#         # sum = hur ** 3+ dec ** 3+ sig ** 3
#         sum = int(num_input[0]) ** 3 + int(num_input[1]) ** 3 + int(num_input[2]) ** 3
#         if sum == int(num_input):
#             print("该数为水仙花数")
#             break
#         else:
#             print("该数不为水仙花数")
#             break
#     else:
#         print("输入数字不合法，请重新输入")

# 纯数字列表排序
lst = [1,2,5,3,8,4,7,51,22,33,44]
lst.sort()
print(lst)
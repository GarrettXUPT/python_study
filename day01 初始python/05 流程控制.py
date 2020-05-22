'''
if 条件语句：
    if 语句块
 当条件成立，执行语句块内容；若条件不成立，则不执行语句块的内容，只看缩进的结果，在其他语言中使用大括号进行分割

'''

#money=int(input("请输入你的钱："))

# if money > 500:
#     print("吃烧烤")
# else: #否则，条件不成立
#     print("不吃饭")
#
# print("没钱了")

# if money > 500:
#     print("吃烧烤")
# elif money > 400:  #数字小于500，但大于400的数
#     print("吃炒饭")
# elif money > 300:
#     print("吃个路边摊")
# else:
#     print("不吃饭")
# print("没钱了")

#if...elif...else... 只要有一个成立，其他的都不再运行，而且依次运行进行判断

#if 嵌套，在语句块中 再次嵌套判断语句

print("guangguangguang")

gender=input("请输入你的性别：")

if gender == "男":   # "="表示赋值 “==”表示判断
    print("去隔壁")
else:
    ask = input(("请问是包租婆吗？"))
    if ask == "是":
        print("滚")
    else:
        print("请进")

#嵌套的层数不要太多，最多3-5层
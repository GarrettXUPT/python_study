# s = "abcdefg"
# s1 = s.capitalize() # 将首字母变成大写，需要返回
# print(s) # 字符串不可变 源字符串不会发生任何改变
# print(s1)

# s = "my name is alex"
# # 单词划分在于 在字符串中出现非字母的东西即为单词分隔符
# s2 = s.title() # 标题 将s中每个单词的首字母大写
# print(s2)

# s = "my name is alex"
# s3 = s.upper() # 将字符串中所有字母变为大写(重点）
# print(s3)
#
# while True:
#     content = input("你想说的话：")
#     content=content.upper()  # 当需要忽略大小写时，可使用该操作
#     if content == "Q":
#         break
#     else:
#         print("你说的话%s" % content)


# 忽略原来大小写问题

# verify_code = "code"
#
# code = input("请输入验证码：")
#
# if code.upper() == verify_code.upper():
#     print("验证码正确")
# else:
#     print("验证码错误")

# 转化小写

# s = "ALEX ENGLISH IS GOOD"
# s4=s.lower() # 有问题 对欧洲的一些特殊的文字是不识别的
# print(s4)

# s = "ALEX ENGLISH IS GOOD"
# s5 = s.casefold() # 可识别欧洲文字将字母变为小写
# print(s5)

#大小写互相转化

# s = "My NAME is Alex"
# s6 = s.swapcase() 大写变小写，小写变大写，将变换以后的字符串进行返回
# print(s6) # mY name IS aLEX


# # center(数字,"_") 居中，第一个为拉长的长度，第二个为以_填充
# s = "Alex"
# s1 = s.center(10,"_") 将s拉长为10个单位长度的内容，并将留白部分由_进行填充
# print(s1)

#去空格

# s = "  ALEX     is   a  good man  "
# ss = "abcdefab"
# s2 = s.strip() # 去掉s两端的空白（空格 \t \n），中间的内容不会变
# s3 = ss.strip("ab") # 去掉ss两端的ab
# print(s3)

# 字符串的替换

# s = "good alex good wusir good daxia good"
# s4 = s.replace("good","shaobing") # 将good替换为shaoping
# s5 = s.replace(" ","") # 一次干掉中间所有的空格
# s6 = s.replace("good","sb",2) # 只替换其中的两个good，且从左往右数
# print(s4)
# print(s5)
# print(s6)

# 字符串的切割

# s = "tai_bai _taihei_wurs_ii_oi"
# s7 = s.split("_") #以_为切点开始切割，切出来的结果会存在列表中
# print(s7)   # ['tai', 'bai ', 'taihei', 'wurs', 'ii', 'oi']
# # 如果切割点在字符串头 那么一定会出现空字符串

# # 格式化输出
# name = "alex"
# age = 18
# hobby = "wusir"
#
# print("我的名字叫%s，今年%d岁。我喜欢%s" % (name,age,hobby))
# print("我的名字叫{}，今年{}岁。我喜欢{}".format(name,age,hobby))
# print("我的名字叫{0}，今年{1}岁。我喜欢{2}".format(name,age,hobby)) # 程序员数数 从来都从0开始数
# print(f"我的名字叫{name}，今年{age}岁，我喜欢{hobby}")
# # 以上四者格式化输出相同，尤其使用第四个


# #查找，判断字符串是否以xxx开头 startwith（）
# s = "java_python_c++_区块链_大数据"
# print(s.startswith("java")) # 判断你的字符串是否以java开头，可以以此作姓氏的分析
#
# # 判断字符串以xxx结尾 endwith（）
# print(s.endswith("大数据"))



# # 计数count（）
#
# s = "123113454321"
# print(s.count("1")) # 数出1在字符串中出现了几次

#查找 find（）若查找内容存在，则返回索引；若不存在，则返回-1. index（） 功能几乎一致，如果找到了，返回索引；若找不不到，则进行报错
# s = "中午吃点啥，吃猪蹄子吧"
# print(s.find("猪")) # 7 若找不到 则返回值为 -1 若找到 则返回其索引值
# print(s.index("猪")) # index若找不到则会报错 需要注意 若找到 也会返回索引值


# # 字符串的判断
# s = "nihaoa 我很好"
# print(s.isalpha()) # 判断字符串是否是以最基本的文字组成（包括汉字与英文） False 内部有空格所以不全是由最基本的文字组成
# s1 = "nihao我很好"
# print(s1.isalpha()) # True
#
# s2 = "1544561"
# print(s2.isdigit()) # 判断是否由阿拉伯数字数字组成，不认识中文数字   True
#
# s3 = "11234一二三"
# print(s3.isnumeric()) # 在这个判断函数中，它是认识中文数字的
#
# s4 = "15654hiudh"
# print(s4.isalnum()) # 判断是否以数字和字母组成 True

# # 判断字符串的长度 len()
#
# s5 = "我叫周润发。我喜欢打DNF"
# print(len(s5)) # 13 len()为内置函数，所有不需要调用，直接可以使用的函数就为内置函数，用来得到字符串的长度

#拿到该句话中的每一个字符

s = "fenhadhiahdiuahdia"
# print(len(s)) s[0] = "f" f[-1] = "a"

## 使用while循环遍历
# i = 0
# while i <= 23:
#     print(s[i])
#     i = i + 1

# 使用for 循环来遍历字符串
# for: 循环
# c: 变量
# in ：固定
# s ： 你要遍历的内容
for c in s: # 把字符串s中的每一个元素分别赋值给前面的c
    print(c)

# for循环有一个先决条件，必须是可迭代对象，缺点是 拿不到其索引，当使用range 就可以拿到其索引值了
'''
for 变量 in 可迭代对象：
    循环体（break， continue）
'''


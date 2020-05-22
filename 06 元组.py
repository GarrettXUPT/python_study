# # 元组使用（）表示，相当于只读列表
# # tu = ("DNF","QQ","facebook","lol",[],{},tuple())
# # # print(tu)
# # # 元组一旦确定就变为不可修改，但是元组也有索引和切片功能，只是不能进行修改
# # print(tu[2:5:2]) # ('facebook', [])

# tu = tuple() # 该表示空元组，固定写法

# # 元祖中如果只有一个元素
# tu = (1 + 1) # 不代表元祖
# print(type(tu)) # <class 'int'>
# tu1 = (1, )  # 该形式表示单个元素的元组 ，单个元素的元组后边要加上逗号，不然会和数字所混淆
# print(type(tu1)) # <class 'tuple'>

# 好习惯：写元组时候，末尾加逗号

# tu = ("DNF","QQ","facebook","lol",[],{},tuple())
# # 元组也是可迭代的，可以使用for循环遍历
# for item in tu:
#     print(item) # 打印出item的值，但是就是不能修改

tu = ("DNF","QQ","facebook","lol",["忍者","神龟"],{},tuple())
# tu[1] = "haha" 不可变 ， 该种形式会报错
tu[4].append("孙悟空") # 元组本身并没有改变，改变的是元组内部的元素，也就是对元组中列表的追加操作是合法的
# tu[4] = ["我是新列表"] 该种形式改变了内部元素的指向，不发生变化
print(tu)


# f = open("葫芦小金刚",mode="r+",encoding="utf-8")
# s = f.read()  # 顺序必须是先读后写
# # r+内容的深坑 只要你读了 写一定是在末尾
# f.write("大娃")
# f.write("二娃")
# f.write("三娃")
# f.write("四娃")
#
# print(s) # 大娃二娃三娃四娃四娃
# f.flush()
# f.close()

# # f = open("葫芦小金刚",mode="w+",encoding="utf-8")
# # # w+ 默认一开始就清空文件，没人用
# # # r+内容的深坑 只要你读了 写一定是在末尾
# # f.write("吐水，吐火")
# # f.seek(0) # 将光标移动至开始端，方便对其进行读取
# # s = f.read()  # 读取的时候 光标已经有写已到末尾，需要重新移动光标
# # print(s) # 吐水，吐火
# #
# # f.flush()
# # f.close()
#
#
#
# # 追加写读，光标在末尾，所有的写 都要在末尾，所以写完以后要读的时候，就要使用seek函数，将光标定位在开头以后，再进行读
# f = open("葫芦小金刚",mode="a+",encoding="utf-8")
# f.write("机器葫芦娃召唤神龙")
# f.seek(0) # 也需要将光标移动至开头
# s = f.read()
# print(s) # 大娃二娃三娃四娃四娃
# f.flush()
# f.close()
lst = []

with open("葫芦小金刚", mode = "r+", encoding = "utf-8") as f:
    lst.append(f.read())
    print(type(f.read()), len(f.read()))

lst1 = []
for ele in lst:
    lst1 = ele.split(",\n")
print(lst1)

lst2 = []
for ele in lst1:
    lst2.append(ele.split(" "))
print(lst2)



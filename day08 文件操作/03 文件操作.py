# # r : read 只读 文件名中有类型后缀 则要添加 若文件名中没有 则不需要添加
# f = open("你要干嘛.txt",mode="r",encoding="utf-8") # pycharm默认为utf-8 文件
# # 读取内容
# # content = f.read() # 全部读取出来
# content1 = f.read(5) # 读取五个字符
# # print(content)# alex 昨晚进入 wusir 的房间，哎呀 我啥也不知知道
# print(content1)  # alex
# f.close()
# print("年后")
#
#
# # # 坑：读取不到内容，因为上面已经读取完毕了，光标在末尾
# # content2 = f.read()
# # print(content2)  # 为空
# #
# # # 良好的操作
# f.close() # 操作完以后，一定要关闭文件连接

f = open("你要干嘛.txt",mode="r",encoding="utf-8")
for i in f: # 把文件中的每一行都读取到i中，
    # print(i.split()) # 去除元素之间的空白，使空白成为列表元素的分隔符
    print(i)
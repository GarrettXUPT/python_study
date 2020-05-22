f = open("胡辣汤",mode = "a",encoding = "utf-8") # a:append()追加，在文件的末尾写入内容 也会创建文件
f.write("你叫什么名字") # 在文件的最末尾，也就是最后一行的后边
f.flush() # 使用该语法刷新文件
f.close()

# with open("胡辣汤", mode="a", encoding = "utf-8") as f1:
#     f1.write("你好")

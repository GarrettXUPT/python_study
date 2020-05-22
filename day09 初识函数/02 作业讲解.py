# # 将文件读出来，并进行打印
# f = open("a1.txt",mode="r",encoding="utf-8")
# s = f.read()
# print(s)
# f.close()

# # 在原文件追加一行内容：不管你信不信，反正我信了
# f = open("a1.txt",mode = "a",encoding="utf-8")
# f.write("不管你信不信，反正我信了")
# f.close()

# 将原文件读出来，并在其后增加一行内容：信不信由你，反正我信了
f = open("a1.txt",mode="r+",encoding="utf-8") # r+ 先读后写

print(f.read())
f.write("信不信由你，反正我信了")
f.close()

# # 将文件清空，然后换上其他内容
# f = open("a1.txt",mode="w",encoding="utf-8")
# f.write("每天努力一点点")
# f.close()


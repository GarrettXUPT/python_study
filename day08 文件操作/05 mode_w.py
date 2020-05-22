# 每次使用w模式打开文件，他都会对该文件进行清空
f = open("胡辣汤",mode = "w",encoding = "utf-8") # 创建文件
f.write("河南特色\n")
f.write("东北特色")

f.flush() # 刷新管道,将数据写入文件
f.close()

# 使用该种语法结构可以省去关闭文件连接的操作
with open("胡辣汤",mode="w",encoding="utf-8") as f:
    f.write("河南特色\n")
    f.write("Garrett")
    print("写入完毕")
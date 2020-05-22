# 需求：将alex换成walker
# 操作步骤：1、先从文件中读取内容
#          2、把要修改的内容进行修改
#          3、把修改好的内容写入新文件
#          4、删除原来的文件 将新文件重新名为原来文件的名字

# 导入os模块 表示操作系统
import os
# f = open("你要干嘛.txt",mode="r",encoding="utf-8")
# f2 = open("你要干嘛（副本）.txt",mode="w",encoding="utf-8")

# with 会帮助我们关闭文件的连接
with open("你要干嘛1.txt", mode = "r",encoding = "utf-8") as f,\
open("你要干嘛（副本）.txt", mode = "w", encoding = "utf-8") as f2:
    for line in f:
        if "alex" in line:
            line = line.replace("alex","walker")
        # print(line) # 得到修改过的信息
        f2.write(line)
# f.close()
# f2.flush()
# f2.close()

# 删除原来的文件
os.remove("你要干嘛1.txt")
# 重命名副本为原来的文件名
os.rename("你要干嘛（副本）.txt","你要干嘛.txt")
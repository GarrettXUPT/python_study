f1 = open("G:/python_study/判断是否位小数.PNG",mode="rb")

f2 = open("G:/python_study/不一定是小数.png",mode="wb")

for line in f1:  # line是从f1中读取的内容
    f2.write(line) # 将从f1中读取的内容，整体写入f2

f1.close()
f2.flush()  # 完成了对文件的复制
f2.close()
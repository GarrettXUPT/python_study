import pickle

class Elephant:
    def __init__(self, name, size, wight, hight):
        self.name = name
        self.size = size
        self.wight = wight
        self.hight = hight

    def chi(self):
        print(f"{self.name}特别喜欢吃")


# e = Elephant("wusir", "12T", "222", "21")
# # # e.chi()
# #
# # # # 序列化
# # # b = pickle.dumps(e)  # 将对象进行序列化
# # # # print(b)
#
# # 反序列化,得到的是原来的对象
# d = pickle.loads(b)
# d.chi()

# e1 = Elephant("wusir", "12T", "222", "21")
# e2 = Elephant("baobao","13T", "123", "32")
#
# f = open("大象", mode="wb")
# # 此处也是序列化
# pickle.dump(e1, f)  # dump表示将对象打散并写入文件 ，序列化以后的内容不是给人看的
# pickle.dump(e2, f)
# f.close()

# f1 = open("大象", mode="rb")
#
# # 读取多个对象
# while 1:
#     try:
#         obj = pickle.load(f1)
#         obj.chi()
#     except Exception:
#         break


# 最佳解决方案,将对象放入列表中，将列表进行序列化

e1 = Elephant("wusir", "12T", "222", "21")
e2 = Elephant("baobao","13T", "123", "32")

lst = [e1, e2]

# f = open("大象", mode="wb")
# # 写入文件
# pickle.dump(lst, f)
# f.close()

f = open("大象", mode="rb")
# 读取文件
obj = pickle.load(f)
for el in obj:
    el.chi()
f.close()
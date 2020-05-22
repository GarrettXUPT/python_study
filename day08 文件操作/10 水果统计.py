# f = open("水果",mode="r",encoding="utf-8")
# line = f.readline().strip() # 第一行内容
# h,i,j,k = line.split(",")
# lst = []
# for line in f:
#     dic = {}
#     line = line.strip()
#     a,b,c,d = line.split(",")
#     dic[h] = a
#     dic[i] = b
#     dic[j] = c
#     dic[k] = d
#     lst.append(dic)
#     #print(dic)
# print(lst)


# vs code里必须使用绝对路径指向文件位置
f = open("G:\python_study\day08 文件操作\水果",mode="r",encoding="utf-8")
line = f.readline().strip() # 第一行内容    编号,名称,价格,数量,哈哈
title = line.split(",")
lst = []
for line1 in f:  # 光标已移至第二行
    dic = {}
    line1 = line1.strip()
    data = line1.split(",")
    for i in range(len(title)):
        dic[title[i]] = data[i]
    lst.append(dic)
    # print(dic)
print(lst)
# [{'编号': '1', '名称': '香蕉', '价格': '1.85', '数量': '50', '哈哈': '22'},
# {'编号': '2', '名称': '苹果', '价格': '2', '数量': '55', '哈哈': '44'},
# {'编号': '3', '名称': '梨子', '价格': '5', '数量': '66', '哈哈': '65'},
# {'编号': '4', '名称': '榴莲', '价格': '5', '数量': '63', '哈哈': '54'}]
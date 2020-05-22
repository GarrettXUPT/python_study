import json

# dic = {"baby":"宝宝", "jay":"周杰伦", "Garrett":True, "Walker":None}
#
# s = json.dumps(dic, ensure_ascii = False)  # json处理中文的问题
#
# # print(s)  # {"baby": "宝宝", "jay": "周杰伦", "Garrett": true, "Walker": null}
# # print(type(s))  # <class 'str'>
#
# d = json.loads(s)
# print(d)  # {'baby': '宝宝', 'jay': '周杰伦', 'Garrett': True, 'Walker': None}
# print(type(d))  # <class 'dict'>


# 将字典写入文件中，一般一个json文件只放置一个字典
dic = {"baby":"宝宝", "jay":"周杰伦", "Garrett":True, "Walker":None}
json.dump(dic, open("字典.json", mode="w", encoding="utf-8"), ensure_ascii=False)
# f.close()

# 将文件中的字典读出
d = json.load(open("字典.json", mode="r", encoding="utf-8"))
print(d)  # {'baby': '宝宝', 'jay': '周杰伦', 'Garrett': True, 'Walker': None}
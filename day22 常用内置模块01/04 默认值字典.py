# from collections import defaultdict
#
# dd = defaultdict(lambda :"胡辣汤")  # 在此处字典是空的
# print(dd["张无忌"])  # 胡辣汤  此处向外拿数据，但字典是空的，key:callable()
# print(dd["宝宝"])  # 这里的中括号和get()不是一回事
# print(dd)  # defaultdict(<function <lambda> at 0x000001CBACE13378>, {'张无忌': '胡辣汤'})


from collections import OrderedDict

dic = OrderedDict()  # 有序字典
dic["a"] = "哈哈"
dic["b"] = "呵呵"
print(dic)  # OrderedDict([('a', '哈哈'), ('b', '呵呵')])

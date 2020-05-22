# def func(a,b):
#     return a + b
# ret = func(1,3)
#
# print(ret) # 4
#
# # 匿名函数统一的名字就是：lambda
# # fn表示函数名，a,b 表示形参 a+b 表示返回值
# fn = lambda a , b : a + b # 可以定义一个很简单的函数，复杂的函数不用lambda
# print(fn(1,3)) # 4

# 使用场景 配合着sorted，map，fliter，一起使用

# sorted 排序函数，让自己去定义排序的规则

# lst = [1,3,2,54,65]
# lst.sort() # 排升序 降序sort(reverse = True)
# print(lst) # [1, 2, 3, 54, 65]
#
# lst1 = [2,3,45,22,4,5565,2]
# s = sorted(lst1)
# print(s) # [2, 2, 3, 4, 22, 45, 5565] 默认升序
#
# lst2 = ["胡一菲","张伟","吕小布","曾小贤"]
# # 按照字符串长度排序
# # 执行流程：把可迭代对象中的每一项拿出来，作为参数传递给后面的key参数，函数返回数字，根据数字进行排序
# # def func(s1):
# #     return len(s1) # 返回长度
# # s = sorted(lst2, key=func) # 内部仍然是按照数字排序的
# # print(s) # ['张伟', '胡一菲', '吕小布', '曾小贤']
#
# s = sorted(lst2,key=lambda s:len(s))
# print(s) # ['张伟', '胡一菲', '吕小布', '曾小贤']

# lst = [{"name":"alex","shengao":"180","tizhong":"88"},
#        {"name":"walker","shengao":"180","tizhong":"70"},
#        {"name":"wusir","shengao":"160","tizhong":"78"},
#        {"name":"alss","shengao":"150","tizhong":"87"},
#        {"name":"ex","shengao":"140","tizhong":"66"}]
# print(sorted(lst,key=lambda dic:dic['shengao']))
# # [{'name': 'ex', 'shengao': '140', 'tizhong': '66'},
# # {'name': 'alss', 'shengao': '150', 'tizhong': '87'},
# # {'name': 'wusir', 'shengao': '160', 'tizhong': '78'},
# # {'name': 'alex', 'shengao': '180', 'tizhong': '88'},
# # {'name': 'walker', 'shengao': '180', 'tizhong': '70'}]

# filter 过滤
# 将可迭代对象打开，把内部元素一个个的传递给前面的函数，由这个函数判断是否应该保留
lst = ["张无忌","周自若","反正","你猜猜","张翠山"]
# 过滤掉姓张的人
f = filter(lambda name:not name.startswith('张'),lst)
print('__iter__'in dir(f))
for el in f:
    print(el)
# 周自若
# 反正
# 你猜猜
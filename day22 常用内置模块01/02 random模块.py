
# from random import randint
#
# print(randint(0, 10))

import random

# print(random.randint(1, 10))  # 产生随机整数
# print(random.random())  # 产生0-1之间的随机小数
#
# print(random.uniform(10, 20))  # 10-20的随机小数
#
# lst = ["宝宝","宝狼","宝强","包拯"]
# random.shuffle(lst)  # 随机打乱顺序
# print(lst)  # ['宝宝', '包拯', '宝强', '宝狼']
#
# # 从列表中随机选择一个
# print(random.choice(["林志玲","刘亦菲","宝宝","石原里美"]))

# 从列表中随机选择三个
print(random.sample(["林志玲","刘亦菲","宝宝","石原里美"], 3))
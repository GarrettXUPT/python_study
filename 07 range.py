# i = 1
# while i<= 100:
#     print(f"当前数字:{i}")
#     i = i + 1

# # range(参数)
# for i in range(10): # range（）是可以迭代的 0-9 从0开始数，满足前闭后开区间
#     print(i)
#
# # range(参数1，参数2)
# for i in range(10,20): #  打印出[参数1，参数2）
#     print(i) 10-19

# # range（参数1，参数2，参数3）
#
# for i in range(10,20,3):    # 打印出[参数1，参数2） 每个参数3个位置取一个数
#     print(i)

lst = ["周杰伦","大风车","葫芦娃","黑猫警长","动画城"]
# for item in lst:   # for循环会丢掉索引
#     print(item)

# 常用此种方法遍历列表，获取到索引及其元素
for i in range(len(lst)):  # i就是索引
    print(i, lst[i]) # 既可以打印出索引，也可以拿到元素
    #  i 就是索引，lst[i] 即为其元素
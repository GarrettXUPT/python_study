import time

# # 时间戳 从1970-01-01 08:00:00 开始计算，未来进行存储及传输的时候使用时间戳
# print(time.time())  # 拿到当前时间1564970763.1607378
#
# # print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 格式化时间，用来显示 2019-08_05 10:06:03
# print(time.strftime("%Y-%m-%d %H:%M:%S  %D %B"))  # 格式化时间，用来显示 2019-08_05 10:06:03 08/05/19 August
# # python时间 ,结构化时间
# print(time.localtime())  # time.struct_time(tm_year=2019, tm_mon=8, tm_mday=5, tm_hour=10, tm_min=11, tm_sec=18, tm_wday=0, tm_yday=217, tm_isdst=0)
#
# t = time.localtime()
# # 拿到当前小时
# print(t.tm_hour) # 10


# # 重点
# # 将数据库里存储的时间还原为格式化时间
# a = 188888888
# # 先把时间戳转化为python中的结构化时间
# t = time.localtime(a)  # 得到结构化时间
# # print(t) # time.struct_time(tm_year=1975, tm_mon=12, tm_mday=27, tm_hour=13, tm_min=8, tm_sec=8, tm_wday=5, tm_yday=361, tm_isdst=0)
# # 将结构化时间转化为格式化时间
# s = time.strftime("%Y-%m-%d %H:%M:%S", t)
# print(s)  # 1975-12-27 13:08:08

# 让用户输入一个时间 将该时间转化为时间戳
user_input = input("请输入一个时间：")
# 将用户输入的字符串转化为结构化时间
struct_time = time.strptime(user_input, "%Y-%m-%d %H:%M:%S")
# 转化为时间戳
t = time.mktime(struct_time)
print(t)
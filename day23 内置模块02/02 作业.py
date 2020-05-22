# # 写一个copy函数，接受两个参数，第一个是源文件位置，另一个是目标位置
# # 将源文件copy到另一个位置
# def copy(sourse, targer):
#     with open(sourse, mode="rb") as f1,\
#         open(targer, mode="wb") as f2:
#         for line in f1:
#             f2.write(line)
#             print(r"adihi")  # 此时，前缀r表示原封不动的输出
#             # 以字节形式进行读取，和以字节形式写入
#     # 此时程序出现的问题是，如果目标文件夹不存在，那么无法创建目标文件


# 此时可完成功能
import os

def copy(sourse, targer):
    # 拿到上级目录
    p = os.path.dirname(targer)
    if not os.path.exists(p):  # 判断目录是否存在，若不存在，则创建目录
        os.makedirs(p)
    with open(sourse, mode="rb") as f1,\
        open(targer, mode="wb") as f2:
        for line in f1:
            f2.write(line)
            print(r"adihi")






# import time
#
# # 计算时间差
# # 算钱的时间——>分钟
# # 显示的时间——>小时，分钟
# start_time = input("请输入起始时间")  # yyyy-mm-dd hh-mm-ss
# end_time = input("请输入结束时间")
#
# # 将输入时间转化为数字
# struct_time_start = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
# struct_time_end = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
#
# # 时间戳
# start = time.mktime(struct_time_start)
# end = time.mktime(struct_time_end)
#
# # 计算时间差
# diff_cs = end - start
# # 计算分钟时间差
# diff_min = diff_cs // 60  # 这个分钟就可以计算金额了
# # 计算小时，显示的分钟
# diff_hour = int(diff_min // 60)
# diff_min_display = int(diff_min % 60)
#
# print(f"经过了{diff_hour}小时{diff_min_display}分钟")

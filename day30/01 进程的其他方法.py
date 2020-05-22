from multiprocessing import Process
import os
import time

# def f1(n):
#     print(f"我是{n}")
#     print("子进程pid", os.getpid())  # 此处查看子进程id
#     print("子进程的副进程的pid", os.getppid())
#
# def f2(n):
#     print(os.getpid())
#     print(f"我是{n}")
#
# if __name__ == '__main__':
#     p1 = Process(target=f1, args=(1,),name="宝宝")
#     p2 = Process(target=f2, args=(2,))
#
#     p1.start()
#     p2.start()
#     print(p1.name)
#     # 查看进程号
#     print("子进程的pid", p1.pid) # 15156
#     print("查看主进程pid", os.getpid())  # 该处查看主进程id


# 其他方法
def f1():
    time.sleep(1)
    print("子进程1号")


if __name__ == '__main__':
    p = Process(target=f1,)
    p.start()

    print("查看该程序是否还在后台运行",p.is_alive()) # True

    p.terminate() # None  给操作系统发送结束进程的信号
    # time.sleep(0.5)
    print(p.is_alive())  # True 在操作系统结束进程即回收内存时，会花费时间，所以主进程中任然显示进程在运行


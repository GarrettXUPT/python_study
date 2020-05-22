from threading import Thread  # 创建线程必调用
from multiprocessing import Process
import os

def f1(n):
    print(f"一号线程任务{n}")
    print('1号pid为%s'%os.getpid())

def f2(n):
    print(f"二号线程任务{n}")
    print('2号pid为%s'%os.getpid())


if __name__ == '__main__':
    t1 = Thread(target=f1, args=(1, ))
    t2 = Thread(target=f2, args=(2, ))
    # 线程运行速度特别快
    t1.start()
    t2.start()
    print('主线程pid为%s'%os.getpid())
    print("主线程结束")
# 上述pid打印结果一致，这些线程同属于一个进程
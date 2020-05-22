# 子进程并发执行
from multiprocessing import Process
import time

def f1(i):
    time.sleep(3)
    print(i)



if __name__ == '__main__':
    for i in range(20):
        p1 = Process(target = f1, args=(i,))  # args为创建进程的传参方式
        p1.start()
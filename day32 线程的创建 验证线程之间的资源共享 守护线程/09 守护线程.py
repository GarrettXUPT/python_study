
# 守护进程：主代码运行结束，守护进程随之结束

# 守护线程：守护进程会等待所有非守护线程运行结束才结束

from threading import Thread
from multiprocessing import Process
import time

def f1():
    time.sleep(4)
    print("一号线程")

def f2():
    time.sleep(3)
    print("二号线程")


if __name__ == '__main__':

    t1 = Thread(target=f1, )
    t2 = Thread(target=f2, )

    # t1.daemon = True  # 设置过守护线程或进程以后，就无法在该进程或线程内再开线程或进程
    # t2.daemon = True  # 当所有的线程执行完毕以后，t2无条件结束运行，不管是否已经运行完毕

    t1.start()
    t2.start()

    print('主线程运行结束')  # 主线程结束以后，如果没有守护线程，则还要为子线程结束做准备，所以不会停止运行，直到子线程也运行结束
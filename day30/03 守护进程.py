# 守护进程：当主进程结束后，子进程都结束
from multiprocessing import Process
import time

def f1():
    # time.sleep(3)
    print("xxx")

def f2():
    time.sleep(2)
    print("普通子进程")

if __name__ == '__main__':
    p1 = Process(target=f1, )
    p1.daemon = True  # 将该进程设置为守护进程，必须写在start前，若主进程代码运行结束，你的子进程无条件跟随结束
    p1.start()

    # p2 为普通子进程，没有进行进程守护操作，所以主进程结束后，但他仍然还在运行
    p2 = Process(target=f2, )
    p2.start()
    p2.join()  # 等待p1进程结束，再运行p2普通进程，最后结束主进程

    # 守护进程会跟着主进程代码运行结束就结束程序运行，不再执行子进程
    print("主进程结束")  # 主进程运行结束后子进程不再打印，因为守护进程作用



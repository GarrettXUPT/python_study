# 子进程并发执行
from multiprocessing import Process
import time

def f1():
    time.sleep(3)
    print("xxx")

def f2():
    time.sleep(3)
    print("sss")

# f1()
# f2()# 该种办法，要执行6秒钟

# windows 系统 必须写main 函数，因为windows创建进程的方式决定的，开启一个子进程，这个
# 子进程会复制一份主进程代码，并且机制类似于import引入，这样就容易导致引入代码时，被引入的
# 代码中的程序被执行，导致递归开启进程
if __name__ == '__main__':  # 该种方法，一共执行3秒钟
    # 在主进程中，开启两个子进程，提高代码运行效率，两个子进程程并发状态，CPU来执行
    p1 = Process(target = f1,)
    p2 = Process(target = f2,)

    p1.start()
    p2.start()

    p1.join()  # join 方法的意思是 等待p1的程序运行完，才继续向下执行
    # p2.join()  # 主进程等待子进程的一种方法

    # p2.start()
    p2.join()  # 等待p2进场结束后，执行主进程
    print("我是主进程")
    # 先打印，因为代码执行速度要比创建进程速度快，因为代码直接由CPU运行，进程由内存创建
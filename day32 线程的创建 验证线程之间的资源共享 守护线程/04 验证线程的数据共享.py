from threading import Thread
# from multiprocessing import Process
import time

num = 100

def f1(n):
    time.sleep(3)
    global num
    num = 3
    print('子线程的num%s'%num)  # 3


if __name__ == '__main__':
    t = Thread(target=f1, args=(1, ))
    t.start()
    t.join()  # 主线程等待子线程执行完毕才会执行主进程中的代码

    print('主线程中的num为%s'%num)  # 3
    # 主线程与子线程中的num打印一致，说明线程之间数据共享
    # 进程之间是空间隔离的，但是多线程属于一个进程，线程之间是可以无障碍通信的
    print("我是主线程")
import time

from multiprocessing import Process

def f1():
    time.sleep(2)
    print("xxx")


if __name__ == '__main__':

    s_time = time.time()
    p = Process(target=f1, )
    p.start()
    p.join()  # 因为主进程运行速度较快，所以必须得等子进程运行完毕以后，才能结束主程序
    e_time = time.time()
    c_time = e_time - s_time
    print("代码运行时间%s"%c_time)

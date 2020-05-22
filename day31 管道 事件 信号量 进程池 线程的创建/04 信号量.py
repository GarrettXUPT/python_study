from multiprocessing import Process, Semaphore
import time
import random

def f1(i, s):
    s.acquire()
    print(f"你好啊{i}")
    time.sleep(random.randint(1, 20))
    s.release()

if __name__ == '__main__':

    s = Semaphore(4)  # 只能同时运行4个进程，计数器为4，acquire一次减一，为0，其他人等待，release，计数器加一
    for i in range(10):  # 创建10个进程
        p = Process(target=f1, args=(i, s,))
        p.start()
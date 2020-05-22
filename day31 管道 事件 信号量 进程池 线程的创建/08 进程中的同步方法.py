from multiprocessing import Process, Pool
import time

def f1(n):
    time.sleep(1)
    # print(n)
    return n**2

if __name__ == '__main__':
    pool = Pool(4)

    for i in range(10):
        print("xxx")
        res = pool.apply(f1, args=(i, ))  # 同步方法，进程一个一个执行，使任务变成了串行  
        print(res)

import os
import time
from multiprocessing import Process, Pool

# def f1(n):
#     time.sleep(2)
#     print(n)

# 对比多进程和进程池的效率，统计100个任务时，多进程和进程池的运行时间
def f1(n):
    for i in range(5):
        n = n + i



if __name__ == '__main__':
    print(os.cpu_count())
    start_time = time.time()

    # 若果不传参数，开启的进程数一般是cpu的核数，该参数指定进程池中有多少个进程时使用
    pool = Pool(4)  # 进程池中放入4个进程，该处4个进程不销毁，当进程完全运行完毕以后，才会将这四个进程结束

    # pool.map(f1, [1, 2])  # pool.map(任务名称, 可迭代的参数),map方法自带join功能
    pool.map(f1, range(100))  # map方法为异步提交任务，在该处100个任务中，只有四个进程在同时工作

    end_time = time.time()

    con_time = end_time - start_time
    print("进程池代码运行时间为%s" % con_time)


    s_time = time.time()
    p_list = []
    for i in range(100):
        p = Process(target=f1, args=(1, ))
        p.start()
        p_list.append(p)

    [pp.join() for pp in p_list]

    e_time = time.time()
    c_time = e_time - s_time
    print("多进程代码运行时间为%s"%c_time)


# 进程池代码运行时间为1.2548608779907227
# 多进程代码运行时间为14.258604049682617

# 多进程的时间很多都花在创建进程和销毁进程上，运行效率较为低下
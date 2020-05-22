# 在IO密集型程序中使用线程会大大提高代码的运行效率，但如果是计算密集型的程序，线程的效率会
# 大大降低，计算密集型程序中，线程的相互切换会降低代码的运行效率，在计算密集型程序中，多进程的
# 运行效率要比多线程大一些因为多线程应用不了多核技术


import time
from threading import Thread
from multiprocessing import Process

def f1():
    time.sleep(1)
    # a = 1
    # a = a + 1
    print('xxx')


if __name__ == '__main__':
    p_s_time = time.time()
    p_list = []
    for i in range(10):
        p = Process(target=f1, )
        p.start()
        p_list.append(p)
    [pp.join() for pp in p_list]
    p_e_time = time.time()
    p_c_time = p_e_time - p_s_time
    print('进程运行时间为%s'%p_c_time)  # 进程运行时间为2.3704373836517334

    t_s_time = time.time()
    t_list = []
    for i in range(20):
        t = Thread(target=f1, )
        t.start()
        t_list.append(t)
    [tt.join() for tt in t_list]
    t_e_time = time.time()
    t_c_time = t_e_time - t_s_time
    print('线程运行时间为%s'%t_c_time)  # 线程运行时间为1.011242389678955,同时开启20个线程

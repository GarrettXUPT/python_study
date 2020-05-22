from multiprocessing import Process, Pool
import time

def f1(i):
    # print(i)
    time.sleep(0.5)
    return i**2

if __name__ == '__main__':

    pool = Pool(4)
    res_list = []

    # pool.apply(f1, args=(2,))  # apply为同步方法,拿到一个数值，只有等到一个该数值，在函数值中运行完，才能开始运行下一个
    for i in range(10):
        # print("任务%s"%i)

        # 进程的同步方法，将任务变成了串行
        # res = pool.apply(f1, args=(i, ))
        # print(res)

        # 进程池的异步方法，异步提交10个任务，由进程池中的4个进程来执行，10个任务会以最快的方式执行完毕
        res = pool.apply_async(f1, args=(i,))
        # as_result = res.get()  # join的效果res为结果对象,res.get表示取结果，再将结果打印，主进程要等着把结果拿到才会执行，变成了串行
        # print(as_result)
        # print(res)
        res_list.append(res)

    pool.close()  # 锁住进程池，不再让其他程序在进程池中加入其他任务，确保没有新的任务交给进程池中的进程
    pool.join()  # 等待进程池中任务执行完以后，再加任务


    for r in res_list:
        print(r.get())
    time.sleep(2)  # 该延时的意义是阻塞主进程，等待进程池中的任务执行完毕
    # 如果主进程运行结束，进程池中的任务全部停止，不会等待进程池中的任务
    print("主进程结束")
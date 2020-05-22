
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor  # 进程池与线程池创建方法
from threading import current_thread  # 可用来获取线程号

def f1(n):
    time.sleep(1)
    print('%s号线程号为%s' % (n, current_thread().ident))

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)  # 若线程池内部不传参，则默认传入，五倍cpu个数的线程池
    pp = ProcessPoolExecutor(4)  # 下方代码不需要修改，就将线程池转化为了进程池

    # tp.map(f1, range(10))  # 使用map异步提交任务，map(子线程，执行任务的个数)
    # print('主线程结束')
    tp_list = []
    for i in range(10):
        res = tp.submit(f1, i)  # 异步提交任务给线程池
        tp_list.append(res)             # 主线程不等待该任务结束就会结束程序的运行，所以使用shutdown来解决
    # print([tp.result for tp in tp_list])

    tp.shutdown()  # 主线程等待全部提交给线程池中的任务全部执行完毕 等于线程池中的close+join
    # time.sleep(5)
    print('主线程结束')
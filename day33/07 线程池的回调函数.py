from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor  # 进程池与线程池创建方法

def f1(n, s):
    return n + s

def f2(n):
    print('回调函数', n.result())  # 使用result来提取结果


if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)

    res = tp.submit(f1, 11, 22).add_done_callback(f2)  # 将f1的运行结果，作为参数传递给f2


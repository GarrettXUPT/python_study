from multiprocessing import Process, Pool

def f1(n):
    return n**2

def call_back_func(s):
    print("回调函数结果%s"%s)


if __name__ == '__main__':
    pool = Pool(4)

    res = pool.apply_async(f1, args=(5, ), callback=call_back_func)  # f1函数的执行结果，直接返回给callback函数

    # pool.close()
    # pool.join()

    print(res.get())
from multiprocessing import Process, Pool
import time

def f1(n):
    time.sleep(0.5)
    # print(n)
    return n**2

if __name__ == '__main__':
    pool = Pool(4)
    res_list = []  # 将异步的结果对象找地方保存
    for i in range(10):  # 这10个任务拿去执行，4个4个进行执行
        print("xxx")
        res = pool.apply_async(f1, args=(i, ))  # 如果使用res.get进行结果的取得，则取得一个结果后才会取下一个，类似于串行得到结果
        res_list.append(res)

    print("等待所有任务执行完毕")
    pool.close()  # 关闭进程池，不让其他程序再往该进程池中提交任务
    pool.join()  # 等待进程池中内容进行完毕

    for r in res_list:  # 从保存列表中取出结果，该种办法，速度很快，执行结果，会直接被计算出来
        print(r.get())


    # time.sleep(10)
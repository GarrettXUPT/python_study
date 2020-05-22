from multiprocessing import Process, Queue

def f1(q):
    q.put("干嘛")  # 子进程放入数据


if __name__ == '__main__':
    q = Queue(3)

    p = Process(target=f1, args=(q, ))
    p.start()

    son_p_msg = q.get()  # 主进程得到数据，取到消息，完成子进程与主进程的相互通信
    print("来自子进程的消息", son_p_msg)
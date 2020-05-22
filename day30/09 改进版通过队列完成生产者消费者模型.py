
from multiprocessing import Process, Queue, JoinableQueue
import time


def producter(q):
    for i in range(10):
        time.sleep(0.5)
        s = '大包子%s号'%i
        print(s+"新鲜出炉")
        q.put(s)
    # q.put(None)  # 发送一个任务结束信号，来中断消费者程序
    q.join()  # 就等着task_done()信号的数量，与put()进去的数量相同时，才继续执行，当计数器减到零时，程序继续执行
    print("所有任务已都被执行完毕，继续执行程序")

def consumer(q):
    while 1:
        time.sleep(1)
        # try:  # 这样其实不合适，应为无法判断到底是做得快还是吃得快，如果吃的快的话，消费者的程序就会直接结束
        #     baozi = q.get_nowait()
        #     print(baozi+"被吃了")
        # except:
        #     print("包子已经吃光了")
        baozi = q.get()
        if baozi == None:
            print("都吃完了")
            break
        print(baozi + "被吃了")
        q.task_done()  # 给队列发送一个取出的任务已经处理完毕的信号，并给计数器减一


if __name__ == '__main__':
    # q = Queue(10)
    # 同样是一个长度为10的队列，JoinableQueue中会有一个类似于计数器的东西，添加
    # 一个数据，计数器就相当于加一，凡是接收到一个taskdone信号，计数器减一
    # 当所有的任务或者数据都放入q中时，就可以通过q来调用join方法，让生产者等着，
    # 就等于让计数器归零，程序才继续执行                             #
    q = JoinableQueue(10)
    pro_p = Process(target=producter, args=(q,))
    con_p = Process(target=consumer, args=(q, ))
    pro_p.start()
    con_p.daemon = True  # 当生产者任务结束，消费者也跟随任务结束，所以设置守护进程
    con_p.start()

    pro_p.join()  # 等待生产者任务处理完毕
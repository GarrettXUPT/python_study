
from multiprocessing import Process, Queue
import time


def producter(q):
    for i in range(10):
        time.sleep(0.5)
        s = '大包子%s号'%i
        print(s+"新鲜出炉")
        q.put(s)
    q.put(None)  # 发送一个任务结束信号，来中断消费者程序

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


if __name__ == '__main__':
    q = Queue(10)

    pro_p = Process(target=producter, args=(q,))
    pro_p.start()

    con_p = Process(target=consumer, args=(q, ))
    con_p.start()
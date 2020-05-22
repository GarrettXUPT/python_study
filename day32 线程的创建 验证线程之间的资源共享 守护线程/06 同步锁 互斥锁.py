
from threading import Thread, Lock
import time
# 该锁的作用与进程中锁的作用相同，都是在牺牲效率，保证数据安全
# 只有加锁才能保证该次执行子线程的安全，以免被其他线程所篡改
num = 100
def f1(l):
    global num
    l.acquire()
    tmp = num
    tmp = tmp - 1
    time.sleep(0.1)
    num = tmp
    l.release()


if __name__ == '__main__':
    l = Lock()

    t_list = []
    for i in range(10):
        t = Thread(target=f1, args=(l, ))
        t.start()
        t_list.append(t)

    [tt.join() for tt in t_list]

    print('主线程的num为%s'%num)
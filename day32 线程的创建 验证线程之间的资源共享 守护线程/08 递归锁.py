# RLock 为递归锁，可解决死锁现象
from threading import Thread, Lock, RLock
import time

def f1(locA, locB):
    locA.acquire()
    print('1号抢到了A锁')
    time.sleep(1)
    locB.acquire()
    print('1号抢到了B锁')
    locB.release()
    locA.release()

def f2(locA, locB):
    locB.acquire()
    print('2号抢到了A锁')
    time.sleep(1)
    locA.acquire()
    print('2号抢到了B锁')
    locA.release()
    locB.release()
# locA被f1抢到，locB被f2抢到，这样f1拿不到locB，f2拿不到locA，导致死锁现象


if __name__ == '__main__':
    locA = locB = RLock()  # 递归锁维护一个计数器，acquire一次加一，release一次减一，当递归锁减到零时，才可继续操作

    t1 = Thread(target=f1, args=(locA, locB, ))
    t2 = Thread(target=f2, args=(locA, locB, ))

    t1.start()
    t2.start()
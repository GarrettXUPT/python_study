
from threading import Thread, Lock
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
    locA = locB = Lock()

    t1 = Thread(target=f1, args=(locA, locB, ))
    t2 = Thread(target=f2, args=(locA, locB, ))

    t1.start()
    t2.start()
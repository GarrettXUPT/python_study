import threading
import gevent
import time

def f1(s):
    print("第一次f1" + s)
    print(threading.current_thread().getName())  # MainThread
    gevent.sleep(2)
    print("第二次f1" + s)

def f2(s):
    print("第一次f2" + s)
    print(threading.current_thread().getName()) # MainThread，任务都在主进程执行
    gevent.sleep(2)
    print("第二次f2" + s)

s = time.time()
g1 = gevent.spawn(f1, 'name')  # 异步提交了一个f1任务
g2 = gevent.spawn(f2, 'gender')  # 异步提交了一个f2任务

# g1.join()
# g2.join()
gevent.joinall([g1, g2])  # 达到上两行代码的效果

e = time.time()
print("程序运行时间为%s" % (e - s))  # 程序运行时间为2.0167524814605713

print("主程序任务")

# 第一次f1name
# MainThread
# 第一次f2gender
# MainThread
# 第二次f1name
# 第二次f2gender
# 主程序任务
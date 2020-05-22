
from threading import Thread, current_thread

def f1(n):
    print('%s号线程任务'%n)
    print('子线程名称', current_thread().getName())  # 子线程名称 Thread-1

def f2(n):
    print('%s号线程任务'%n)
    print('子线程名称', current_thread().getName())  # 子线程名称 Thread-2

if __name__ == '__main__':
    t1 = Thread(target=f1, args=(1, ))
    t1.start()

    t2 = Thread(target=f2, args=(2, ))
    t2.start()

    print('主线程名称', current_thread().getName())  # 主线程名称 MainThread
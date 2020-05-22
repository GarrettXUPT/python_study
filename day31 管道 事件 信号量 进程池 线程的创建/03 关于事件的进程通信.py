from multiprocessing import Process, Event
import time

def f1(e):
    time.sleep(2)
    n = 100
    print(f"子进程计算结果为{n}")
    e.set()

if __name__ == '__main__':
    e = Event()
    p = Process(target=f1, args=(e,))
    p.start()

    print("主进程等待......")
    e.wait()
    print("结果已经写入文件")
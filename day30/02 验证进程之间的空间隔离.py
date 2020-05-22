# 验证进程之间的空间隔离，若全局变量遭到修改，那么说明没有进行空间隔离，反之，说明空间隔离

from multiprocessing import Process
import time

num = 100

def f1():
    global num
    num = 3
    print("子进程中的num", num)

print(">>>>>>", num) # 100 此处是因为f1函数并没有执行


if __name__ == '__main__':
    p1 = Process(target=f1,)
    p1.start()
    p1.join()
    print("主进程中的num", num)  # 100

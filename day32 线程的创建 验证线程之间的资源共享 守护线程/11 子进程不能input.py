
# 子进程不能进行input，但是主进程可以

# from multiprocessing import Process
#
# def f1():
#     # i = input("请输入")  # EOFError: EOF when reading a line
#     pass
#
# if __name__ == '__main__':
#     # i = input("主进程input：")
#     p = Process(target=f1, )
#     p.start()


# 线程

from threading import Thread

def f1():
    name = input("请输入你的名字")
    print("子线程输入的名字为%s"%name)


if __name__ == '__main__':
    t = Thread(target=f1, )
    t.start()
    zhu = input("主线程输入内容")
    print("主线程输入的内容为：%s"%zhu)  # 该种情况下，当然优先输入主线程中的输入内容


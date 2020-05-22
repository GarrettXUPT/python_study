
# 第一种

from threading import Thread  # 创建线程必调用
from multiprocessing import Process

# def f1(n):
#     print(f"一号线程任务{n}")
#
# def f2(n):
#     print(f"二号线程任务{n}")
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=f1, args=(1, ))
#     t2 = Thread(target=f2, args=(2, ))
#     # 线程运行速度特别快
#     t1.start()
#     t2.start()

    # print("主线程")

class My_thread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 此处run方法仍然不可变
        print(f"你好啊,{self.name}")

if __name__ == '__main__':
    t = My_thread("葫芦娃")
    t.start()

    print("主线程结束")
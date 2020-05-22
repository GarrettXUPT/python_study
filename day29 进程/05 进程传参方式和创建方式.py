from multiprocessing import Process
import time

# def f1(n):
#     print(n)
#
# def f2(n):
#     print(n)

# # 演示两种传参方式
# if __name__ == '__main__':
#     p1 = Process(target=f1, args=("大力与奇迹",))  # 创建进程对象
#     p2 = Process(target=f2, kwargs={'n':'大力与奇迹'})  # 创建进程对象
#     p1.start()  # 给操作系统发送创建进程的信号，后续进程的创建都由操作系统完成
#     p2.start()


# 进程的创建方式2,以面向对象方式

class MyProcess(Process):
    def __init__(self, n):
        super().__init__()  # 执行父类中的_init__

        self.n = n

    def run(self):  # 此处run方法不可改
        print(f"宝宝and{self.n}")


if __name__ == '__main__':
    # 传参
    p1 = MyProcess('高温')
    p1.start()
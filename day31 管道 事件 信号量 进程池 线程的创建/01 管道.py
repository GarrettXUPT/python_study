# 管道类似于进程间的通信,管道直接在进程之间相互通信

from multiprocessing import Process, Pipe

def f1(conn):
    from_zhujinc_recv = conn.recv()
    print("我是子进程")
    print(f"来自主进程的消息{from_zhujinc_recv}")

if __name__ == '__main__':
    conn1, conn2 = Pipe()  # 创建一个管道对象，返回管道的两端，全双工工作模式，返回管道的两端，但是只能一段进一端出

    # 可以将一端或者两端发送给其他进程，许多进程就可以通过这一个管道进行通信
    conn1.send("你干嘛")
    p1 = Process(target=f1, args=(conn2,))
    p1.start()

    print("我是主进程")
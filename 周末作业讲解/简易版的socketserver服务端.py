# 模拟socketserver() 模块
import socket
from threading import Thread

class MySocket:
    def __init__(self, server_addr):
        self.server_addr = server_addr
        self.socket = socket.socket()
    # 绑定了ip地址和接口，监听，执行了建立连接的方法
    def server_forever(self):
        self.socket.bind(self.server_addr)
        self.socket.listen(5)
        self.build_connect()
    # 建立连接，将建立连接过程循环起来，因为我们每次建立连接都要开一个线程去运行它，通过这个连接收发消息
    def build_connect(self):
        while 1:
            # 让主线程代码循环起来，要让accept方法和handle方法，异步运行，不然建立连接这个循环将无法执行，因为handle也是循环
            conn, addr = self.socket.accept()
            # 开启线程处理conn，一个线程一个conn
            t = Thread(target=self.handle, args=(conn, ))
            t.start()
    # 收发消息的内容，每个线程都要执行一下handle方法，将conn作为参数传给handle方法
    def handle(self, conn):
        while 1:
            from_client_msg = conn.recv(1024).decode('utf-8')
            print("来自客户端的消息:%s" % from_client_msg)

            to_client_msg = input("发送至客户端的消息为:")
            conn.send(to_client_msg.encode('utf-8'))



if __name__ == '__main__':
    ip_port = ('192.168.0.107', 8001)

    server =  MySocket(ip_port)
    server.server_forever()
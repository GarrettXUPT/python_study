import socketserver
# 解决多用户登陆问题
class My_server(socketserver.BaseRequestHandler):
    def handel(self):  # 该处handel方法名，不可变，因为底层就是调用该方法
        while 1:
            from_client_msg = self.request.recv(1024)  # self.request == conn
            print(from_client_msg.decode('utf-8'))
            To_client_msg = input("嘻嘻说：")
            self.request.send(To_client_msg.encode('utf-8'))


if __name__ == '__main__':
    ip_port = ('192.168.43.39',8002)
    server = socketserver.ThreadingTCPServer(ip_port, My_server)
    server.serve_forever()



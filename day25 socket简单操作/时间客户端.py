# 客户端向服务端发送时间
import socket
import time

client = socket.socket()

server_ip_port = ('192.168.43.39',8001)

client.connect(server_ip_port)

while 1:
    client.send(str(time.time()).encode('utf-8'))
    time.sleep(1)
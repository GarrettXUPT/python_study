import socket

BUFFSIZE = 1024
ip_port = ('192.168.43.39',8001)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

res = s.connect(ip_port)

s.send("hi".encode('utf-8'))
s.send("nihao".encode('utf-8'))
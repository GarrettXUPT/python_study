

import socket

client = socket.socket()
client.connect(('192.168.0.107', 8001))

while 1:
    to_server_msg = input("发送至服务端的消息:")
    client.send(to_server_msg.encode('utf-8'))

    from_server_msg = client.recv(1024).decode('utf-8')
    print("来自服务端的消息:%s" % from_server_msg)
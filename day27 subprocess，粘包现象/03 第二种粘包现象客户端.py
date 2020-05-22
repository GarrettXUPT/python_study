# import socket
#
# client = socket.socket()
#
# client.connect(('192.168.43.39',8001))
#
# while 1:
#
#     cmd = input("请输入指令：")
#
#     client.send(cmd.encode('utf-8'))
#
#     from_server_msg = client.recv(1024)
#
#     print(from_server_msg.decode('gbk'))

# 解决方案1

# import socket
#
# client = socket.socket()
#
# client.connect(('192.168.43.39',8001))
#
# while 1:
#
#     cmd = input("请输入指令：")
#
#     client.send(cmd.encode('utf-8'))
#
#     from_server_msg_len = client.recv(1024)
#     print("来自服务端的消息长度", int(from_server_msg_len.decode('utf-8')))
#
#     client.send(b'ok')  # 发送给服务端，表示已经收到了信息长度
#
#     from_server_msg = client.recv(int(from_server_msg_len))
#
#     print(from_server_msg.decode('gbk'))


# 解决方案2

import socket
import struct

client = socket.socket()

client.connect(('192.168.43.39',8001))

while 1:

    cmd = input("请输入指令：")

    client.send(cmd.encode('utf-8'))
    # 接收数据长度，首先接受4个数据长度的数据，因为这四个字节是长度
    from_server_msg_len = client.recv(4)
    msg_len = struct.unpack('i', from_server_msg_len)[0]
    # 通过解包出来的长度，来接收后面的真实数据
    from_server_msg = client.recv(msg_len)

    print(from_server_msg.decode('gbk'))
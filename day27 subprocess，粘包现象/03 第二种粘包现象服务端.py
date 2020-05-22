# import socket
# import subprocess
#
# server = socket.socket()
# ip_port =('192.168.43.39',8001)
#
# server.bind(ip_port)
#
# server.listen(5)
#
# conn, addr = server.accept()
#
# while 1:
#     from_lient_cmd = conn.recv(1025)
#     print(from_lient_cmd.decode('utf-8'))
#
#     sub_obj = subprocess.Popen(
#         from_lient_cmd.decode('utf-8'),
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )
#     std_msg = sub_obj.stdout.read()
#     print("指令的执行结果长度----》", len(std_msg))
#     conn.send(std_msg)

# 解决方案1

# import socket
# import subprocess
#
# server = socket.socket()
# ip_port =('192.168.43.39',8001)
#
# server.bind(ip_port)
#
# server.listen(5)
#
# conn, addr = server.accept()
#
# while 1:
#     from_lient_cmd = conn.recv(1025)
#     print(from_lient_cmd.decode('utf-8'))
#     # 接收到客户端发送来的系统指令，服务端通过subprocess模块进行执行，到服务端自己的系统中执行该指令
#     sub_obj = subprocess.Popen(
#         from_lient_cmd.decode('utf-8'),
#         shell=True,
#         stdout=subprocess.PIPE,  # 正确结果的存放位置
#         stderr=subprocess.PIPE   # 错误结果的存放位置
#     )
#     # 从管道中拿出结果，通过subprocess.Popen的实例化对象，stdout.read()方法来获取管道中的结果
#     std_msg = sub_obj.stdout.read()
#     # 未解决粘包现象，统计消息的长度，先将消息的长度发送给客户端，客户端通过该长度来接收要发送的真实数据
#     std_msg_len = len(std_msg)
#     # 首先将数据长度的数据类型转化为bytes类型
#     std_bytes_len = str(std_msg_len).encode('utf-8')  # 要发送的是bytes类型，所以将数据转化为bytes类型
#     print("指令的执行结果长度----》", len(std_msg))
#     conn.send(std_bytes_len)
#     status = conn.recv(1024)
#     if status.decode('utf-8') == 'ok':
#         conn.send(std_msg)
#     else:
#         pass


# 解决方案2

import socket
import subprocess
import struct

server = socket.socket()
ip_port =('192.168.43.39',8001)

server.bind(ip_port)

server.listen(5)

conn, addr = server.accept()

while 1:
    from_lient_cmd = conn.recv(1025)
    print(from_lient_cmd.decode('utf-8'))
    # 接收到客户端发送来的系统指令，服务端通过subprocess模块进行执行，到服务端自己的系统中执行该指令
    sub_obj = subprocess.Popen(
        from_lient_cmd.decode('utf-8'),
        shell=True,
        stdout=subprocess.PIPE,  # 正确结果的存放位置
        stderr=subprocess.PIPE   # 错误结果的存放位置
    )
    # 从管道中拿出结果，通过subprocess.Popen的实例化对象，stdout.read()方法来获取管道中的结果
    std_msg = sub_obj.stdout.read()
    # 未解决粘包现象，统计消息的长度，先将消息的长度发送给客户端，客户端通过该长度来接收要发送的真实数据
    std_msg_len = len(std_msg)
    print('数据长度',std_msg_len)
    msg_lenint_struct = struct.pack('i', std_msg_len)

    # bytes类型数据可以做加法拼接的
    conn.send(msg_lenint_struct+std_msg)

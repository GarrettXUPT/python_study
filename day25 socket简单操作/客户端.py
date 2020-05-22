# 导入socket模块
import socket
# 创建socket对象
client = socket.socket()
# 找到服务端的IP地址和端口
server_ip_port = ('192.168.43.39',8001)
# 连接服务端中的应用程序，通过connet方法，参数是服务端的IP地址和端口
client.connect(server_ip_port)
# 发消息，使用send方法，但调用的是socket对象
# client.send(b"hello")
while 1:

    To_server_msg = input("对方说：")
    client.send(To_server_msg.encode("utf-8"))

    from_server_msg = client.recv(1024)
    print("你说：",from_server_msg.decode("utf-8"))
# 关闭客户端
# client.close()
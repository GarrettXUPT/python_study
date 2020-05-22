# 导入socket模块
import socket  # 任何语言做网络通信的项目，必须使用socket
# 创建socket对象，创建了一个通信设备服务端
server = socket.socket()
# 给程序设置一个IP地址和端口号
ip_port = ('192.168.43.39',8001)  # 服务端IP地址端口，创建端口地址端口
# 绑定IP地址和端口
server.bind(ip_port)

# 监听IP地址和端口号，并输入可等待设备的数目
server.listen(5)

# 等待建立连接，conn是连接通道，addr是客户端的的IP地址
conn, addr = server.accept()
while 1:
    # 服务端通过conn进行收发消息，通过recv方法，recv里的参数是字节(B) 1024的意思是1024B = 1KB，该次接收到的消息大小为1KB
    from_client_msg = conn.recv(1024)
    # 打印接收到的消息
    print("对方说：",from_client_msg.decode("utf-8"))
    # 回复消息，通过send方法，但是send方法中，参数必须是字节类型的
    # conn.send(b"nigui,suannihen") # 发送英文
    To_client_msg = input("你说：")
    conn.send(To_client_msg.encode("utf-8"))
# 关闭通道，通过close方法
# conn.close()
# # 关闭socket对象
# server.close()
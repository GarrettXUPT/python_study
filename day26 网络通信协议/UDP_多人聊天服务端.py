import socket
# 基于UDP协议的网络通信
udp_server = socket.socket(type = socket.SOCK_DGRAM) # datagram

ip_port = ('192.168.0.107',8001)

udp_server.bind(ip_port)

while 1:

    from_client_msg, client_address = udp_server.recvfrom(1024)  # 1024的传输速度是最快的

    print(from_client_msg.decode('utf-8'), client_address)

    To_client_msg = input("服务端说:")

    udp_server.sendto(To_client_msg.encode('utf-8'), client_address) # 回复客户端，向得到的客户端进行发送数据包



    # b'hello' ('192.168.43.39', 50494) 信息与客户端地址
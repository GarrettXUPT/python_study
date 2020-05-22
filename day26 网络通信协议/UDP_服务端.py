import socket
# 基于UDP协议的网络通信
udp_server = socket.socket(type = socket.SOCK_DGRAM) # datagram

ip_port = ('192.168.43.39',8001)

udp_server.bind(ip_port)

from_client_msg, client_address = udp_server.recvfrom(1024)  # 1024的传输速度是最快的

udp_server.sendto(b'gunduzi', client_address) # 回复客户端，向得到的客户端进行发送数据包

print(from_client_msg, client_address)

# b'hello' ('192.168.43.39', 50494) 信息与客户端地址
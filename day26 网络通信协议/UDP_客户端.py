import socket

udp_client = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('192.168.43.39',8001)

udp_client.sendto(b'hello', ip_port)

from_server_msg, server_address= udp_client.recvfrom(1024)

print(from_server_msg, server_address)

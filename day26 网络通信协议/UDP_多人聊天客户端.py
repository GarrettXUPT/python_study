import socket

udp_client = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('192.168.0.107',8001)

while 1:
    
    To_server_msg = input("客户端说：")

    udp_client.sendto(To_server_msg.encode('utf-8'), ip_port)

    from_server_msg, server_address= udp_client.recvfrom(1024)

    print(from_server_msg.decode('utf-8') ,server_address)
    

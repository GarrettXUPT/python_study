import socket

client = socket.socket()

server_ip_port = ('192.168.43.39',8001)

client.connect(server_ip_port)

while 1:

    To_server_msg = input("宝宝：")

    client.send(To_server_msg.encode('utf-8'))

    if To_server_msg == "byebye":
        break

    from_server_msg = client.recv(1024)

    print("宝浪说：", from_server_msg.decode('utf-8'))

client.close()
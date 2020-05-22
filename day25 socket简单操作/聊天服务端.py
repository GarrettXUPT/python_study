import socket

server = socket.socket()  # TCP协议的网络通信

ip_port = ('192.168.43.39',8001)

server.bind(ip_port)

server.listen()

conn,addr = server.accept()

while 1:
    from_client_msg = conn.recv(1024)

    print("宝宝说：", from_client_msg.decode('utf-8'))

    To_client_msg = input("宝浪说：")

    conn.send(To_client_msg.encode('utf-8'))